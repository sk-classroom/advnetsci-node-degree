import numpy as np
import sys
import os
import igraph
from scipy import sparse
import pandas as pd
import heapq

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from assignment.assignment import estimate_platform_distribution

def estimate_naive_platform_distribution(survey_data):
    """
    Estimate the unbiased distribution of social media platform preferences using degree-based correction.

    Args:
        survey_data (pandas.DataFrame): pandas.DataFrame for survey responses consisting of platform names, degree, and participant IDs.

    Returns:
        list of tuples: Unbiased estimate as [(platform, percentage), ...] e.g., [("Facebook", 0.3), ("Instagram", 0.2), ("LinkedIn", 0.1), ...]

    """

    counts = survey_data.groupby("platform").size().to_dict()

    total = survey_data["platform"].shape[0]

    result = [
        (platform, counts[platform] / total) for platform in counts.keys()
    ]
    return result


def run_percolation(graph, seed, edge_prob):
    """
    Find the minimum spanning tree (MST) of a graph using Prim's algorithm,
    starting from the specified seed node.

    Parameters:
        graph: igraph.Graph
            The input undirected, weighted graph.
        seed: int
            The index of the starting node.

    Returns:
        mst_graph: igraph.Graph
            The MST as an igraph.Graph object, with the same node ids as the input.
    """

    n = graph.vcount()
    if isinstance(seed, int):
        seed = [seed]
    visited = set(seed)
    mst_edges = []
    edge_heap = []

    # Add all edges from the seed node to the heap
    for s in seed:
        for neighbor in graph.neighbors(s):
            eid = graph.get_eid(s, neighbor)
            weight = (
                graph.es[eid]["weight"]
                if "weight" in graph.es.attributes()
                else 1.0
            )
            heapq.heappush(edge_heap, (weight, s, neighbor))

    while len(visited) < n and edge_heap:
        weight, u, v = heapq.heappop(edge_heap)
        if np.random.rand() > edge_prob:
            continue
        if v in visited:
            continue
        # Add edge to MST
        mst_edges.append((u, v, weight))
        visited.add(v)
        # Add all edges from the new node to the heap
        for neighbor in graph.neighbors(v):
            if neighbor not in visited:
                eid = graph.get_eid(v, neighbor)
                w = (
                    graph.es[eid]["weight"]
                    if "weight" in graph.es.attributes()
                    else 1.0
                )
                heapq.heappush(edge_heap, (w, v, neighbor))

    # Create MST igraph object with the same node ids and attributes
    mst_graph = igraph.Graph()
    mst_graph.add_vertices(graph.vcount())
    # Copy vertex attributes
    for attr in graph.vs.attributes():
        mst_graph.vs[attr] = graph.vs[attr]
    # Add edges and weights
    mst_graph.add_edges([(u, v) for u, v, w in mst_edges])
    if "weight" in graph.es.attributes():
        mst_graph.es["weight"] = [w for u, v, w in mst_edges]
    return mst_graph

# Generate network based on slider values (reactive to changes)
def run_simulation(
    g,
    initial_sample_size,
    participation_prob,
    alpha,
    bias_expo,
    platform_list,
):
    np.random.shuffle(platform_list)
    # g = igraph.Graph.Barabasi(n=n_nodes, m=m)
    A = g.get_adjacency_sparse()
    citing, cited, _ = sparse.find(A)
    n_nodes = g.vcount()

    _deg = np.array(g.degree())
    _deg_norm = _deg / np.max(_deg)

    platform_bias = np.random.rand(len(platform_list)) ** bias_expo
    platform_bias /= np.max(platform_bias)

    # P is the probability of a node choosing a platform
    P = np.exp(np.outer(_deg_norm, platform_bias) / alpha)
    P /= np.sum(P, axis=1, keepdims=True)
    gumbel = np.random.gumbel(size=P.shape)
    preference_platform_ids = np.argmax(np.log(P) + gumbel, axis=1)
    preferences = np.array(platform_list)[preference_platform_ids]

    # Simulate network survey sampling (friend recruitment)
    survey_participants = []
    survey_data = []

    # Step 1: Start with random initial sample
    total_nodes = g.vcount()
    initial_participants = np.random.choice(
        total_nodes, size=initial_sample_size, replace=False
    ).tolist()

    # Step 2: Percolate the network by removing each edge with probability 1-p
    g_perc = run_percolation(g, initial_participants, participation_prob)

    # Step 3: For each initial participant, get their connected component in the percolated graph
    membership = np.array(g_perc.connected_components(mode="weak").membership)
    # Find all unique component ids for the initial participants
    component_ids = np.unique(membership[initial_participants])
    # All nodes in any of these components are participants
    participants = np.where(np.isin(membership, component_ids))[0]

    # Step 4: Collect survey responses
    degree = np.array(g.degree())

    survey_data = pd.DataFrame(
        {
            "participants": participants,
            "platform": preferences[participants],
            "degree": degree[participants],
        }
    )
    return g_perc, preferences, survey_data, initial_participants


def run_estimators(naive_estimator, focal_estimator, simulation_results, platform_names):
    result_tables = []
    errors = []
    for _i, result in enumerate(simulation_results):
        # True population distribution (ground truth from all nodes)
        # node_platform_preferences is a numpy array of all node preferences
        _true_counts = (
            pd.Series(result["node_platform_preferences"])
            .value_counts()
            .reindex(platform_names, fill_value=0)
        )
        _true_total = _true_counts.sum()
        _true_prop = _true_counts / _true_total

        # Naive estimate: just raw survey proportions (from survey_data)
        _naive_result = naive_estimator(
            result["survey_data"]
        )
        _naive_df = (
            pd.DataFrame(_naive_result, columns=["platform", "proportion"])
            .set_index("platform")
            .reindex(platform_names, fill_value=0)
        )
        _naive_prop = _naive_df["proportion"].values

        # Corrected estimate using the student's function
        _corrected_result = focal_estimator(
            result["survey_data"]
        )
        _corrected_df = (
            pd.DataFrame(_corrected_result, columns=["platform", "proportion"])
            .set_index("platform")
            .reindex(platform_names, fill_value=0)
        )
        _corrected_dist = _corrected_df["proportion"].values

        # Create master table
        _result_table = pd.DataFrame(
            {
                "True Proportion": _true_prop,
                "Naive Proportion": _naive_prop,
                "Estimated Proportion": _corrected_dist,
            },
            index=platform_names,
        )
        result_tables.append(_result_table)
        # Compute errors
        _naive_error = np.mean((_naive_prop - _true_prop) ** 2)
        _corrected_error = np.mean((_corrected_dist - _true_prop) ** 2)
        errors.append({"estimator": "naive", "MSE": _naive_error, "sample_id": _i})
        errors.append({"estimator": "corrected", "MSE": _corrected_error, "sample_id": _i})
    error_table = pd.DataFrame(errors)
    return result_tables, error_table


def run_multiple_simulations(naive_estimator, focal_estimator, n_simulations=10):
    # Number of edges to attach from a new node to existing nodes in the Barabási–Albert model
    m = 2

    # Total number of nodes in the generated network
    n_nodes = 3000

    # Number of initial "seed" participants in the RDS simulation
    initial_sample_size = 5

    # Probability that a recruited friend will participate in the survey
    participation_prob = 0.15

    # Alpha parameter controls the strength of hubs' preference towards popular platforms. Lower value leads to a stronger preference bias.
    alpha = 1e-2

    # Exponent for biasing the platform preference distribution (higher = more skewed)
    bias_expo = 2.0

    # Generate the underlying social network using the Barabási–Albert preferential attachment model
    g_backborn = igraph.Graph.Barabasi(n=n_nodes, m=m)

    platform_list = [
        "Facebook",
        "X",
        "Instagram",
        "TikTok",
        "LinkedIn",
        "YouTube",
    ]

    simulation_results = []
    for _ in range(n_simulations):
        while True:
            (
                _g_perc,
                _node_platform_preferences,
                _survey_data,
                _initial_participants,
            ) = run_simulation(
                g=g_backborn,
                initial_sample_size=initial_sample_size,
                participation_prob=participation_prob,
                alpha=alpha,
                bias_expo=bias_expo,
                platform_list=platform_list,
            )
            if len(_survey_data) > 200:
                break

        simulation_results.append(
            {
                "node_platform_preferences": _node_platform_preferences,
                "survey_data": _survey_data,
                "initial_participants": _initial_participants,
                "g_perc": _g_perc,
            }
        )
    return run_estimators(naive_estimator, focal_estimator, simulation_results, platform_list)