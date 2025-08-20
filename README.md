# Network Immunization Strategy Assignment

[![Open in Cloud Marimo](https://img.shields.io/badge/Open%20in-Cloud%20Marimo-blue)](https://pyodide.marimo.io/?c=I8r9R4g9FKVJ8v8K)

This assignment focuses on implementing and evaluating vaccination strategies to maximize transmission route removal in networks. You'll explore how network structure influences the effectiveness of different immunization approaches and compare strategies based on their ability to remove network transmission capacity.

## 🎯 Learning Objectives

By completing this assignment, you will:

1. **Implement vaccination strategies**: Learn random and degree-based node selection for immunization
2. **Calculate transmission routes removed**: Understand how vaccination reduces network transmission capacity
3. **Evaluate strategy effectiveness**: Compare vaccination approaches using the 1.5x improvement benchmark
4. **Apply network theory**: Connect degree centrality to epidemic control strategies

## 📋 Assignment Tasks

### Task 1: Random Vaccination Strategy (25 points)
Implement `random_vaccination_strategy(g, num_vaccines)` to select nodes randomly for vaccination.

### Task 2: Degree-Based Vaccination Strategy (25 points)
Implement `degree_based_vaccination_strategy(g, num_vaccines)` to target highest-degree nodes for vaccination.

### Task 3: Transmission Routes Calculation (25 points)
Implement `calculate_transmission_routes_removed(g, vaccinated_nodes)` to calculate total transmission routes removed by vaccination.

### Task 4: Strategy Evaluation (25 points)
Implement `evaluate_vaccination_strategy(g, strategy_func, ...)` to evaluate strategies using the 1.5x improvement benchmark.

## 🚀 Workflow

1. Read the assignment instruction in [assignment/README.md](assignment/README.md)
2. Complete the assignment notebook (assignment/assignment.py). You have several options to do this:
  - (Recommended) Run `uv run marimo edit --sandbox assignment/assignment.py` in your terminal
  - Alternatively,
    - 1. Open the assignment in Cloud Marimo (Molab)
    - 2. Fork the notebook and complete the assignment. (You'll need to create an account on MoLab)
3. Complete [the quiz](assignment/quiz.toml)
4. Git add, commit, push the notebook. If you are not sure what they are, [here is a guide](https://graphite.dev/guides/git-add-commit-push)
5. The assignment will be auto-graded, and you can check out the results at [Github Action](https://docs.github.com/en/education/manage-coursework-with-github-classroom/learn-with-github-classroom/view-autograding-results)

## 💻 Computing Environment

### GitHub Classroom (Recommended)
You can use GitHub Codespaces to complete the assignment. Note that this environment is not permanent and will be deleted after the course finishes. You can keep files in the codespace by git-pushing them to the repository.

### Local Machine
You can download the repo and work locally on your machine. Using "git clone" is the easiest way to do this.

## 🧪 Testing Your Work

The assignment includes:
- **Interactive dashboard**: Real-time testing and strategy comparison on different network types
- **Comprehensive test suite**: Run individual test files to verify correctness
- **Visual feedback**: 4-panel dashboard showing transmission routes removed, improvement factors, and vaccination target distributions

## 📚 Key Concepts

### Vaccination Strategies
- Random selection as baseline comparison
- Degree-based targeting of network hubs
- Strategic node selection for epidemic control

### Transmission Route Analysis
- Calculate total transmission capacity removed by vaccination
- Sum of degrees of vaccinated nodes as effectiveness metric
- Direct measurement of network disruption

### Strategy Evaluation
- Improvement factor calculation (strategy vs random)
- 1.5x threshold for meaningful improvement
- Comparative analysis across network types

### Network Epidemiology
- Hub-based epidemic control
- Acquaintance immunization and friendship paradox
- Real-world applications to public health policy

## 🏆 Grading

- **Correctness (70%)**: Functions produce correct outputs on test cases
- **Quiz (20%)**: Conceptual understanding of network epidemiology
- **Code Quality (10%)**: Clean, efficient implementations

## 🎮 Interactive Features

The assignment includes a vaccination strategy comparison dashboard that lets you:
- Test implementations on different network types (scale-free, random, small-world, regular)
- Compare vaccination strategies across network models
- Visualize transmission routes removed and improvement factors
- Explore how network structure affects strategy performance

## 📊 Network Types

Your implementations will be tested on:
- **Barabási-Albert (Scale-free)**: Clear hubs make degree-based vaccination highly effective
- **Erdős-Rényi (Random)**: Homogeneous structure reduces degree-based advantage
- **Watts-Strogatz (Small-world)**: Intermediate structure with clustered connectivity
- **Regular Lattices**: Minimal degree variance, strategies perform similarly

## 🔍 Debugging Tips

1. **Start simple**: Test functions on tiny graphs you can verify by hand
2. **Use the dashboard**: Visual feedback helps identify implementation errors
3. **Check edge cases**: All vaccinated networks, isolated nodes, complete graphs
4. **Verify properties**: Degree sum calculations, improvement factor thresholds

## 🚫 Academic Integrity

- Write your own implementations
- You may discuss concepts but not share code
- Cite any external resources used
- AI assistance must be acknowledged in comments

## 📖 Resources

- Course lecture notes on node degree and network immunization
- Interactive vaccination games for transmission route concepts
- Network science literature on degree centrality and targeted interventions
- Research on acquaintance immunization and friendship paradox applications

---

**Need Help?** Check the course discussion forum or attend office hours. For technical issues, create an issue in this repository.