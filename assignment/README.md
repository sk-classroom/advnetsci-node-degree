# Network Immunization Strategy Assignment

## Overview

This assignment focuses on implementing and evaluating vaccination strategies to maximize transmission route removal in networks. You'll explore how network structure influences the effectiveness of different immunization approaches and test strategies based on their ability to remove network transmission capacity.

## Learning Objectives

By completing this assignment, you will:

1. **Implement vaccination strategies**: Learn random and degree-based node selection for immunization
2. **Calculate transmission routes removed**: Understand how vaccination reduces network transmission capacity
3. **Evaluate strategy effectiveness**: Compare vaccination approaches using the 1.5x improvement benchmark
4. **Apply network theory**: Connect degree centrality to epidemic control strategies

## Assignment Tasks

### Task 1: Function Implementation (100 points)

<p align="center">
  <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDC8T-6_7wMK9PWpXbRm7FUU2iMMhvAE0YFYX9RcA4PXLGNDJJFW6anUa4tBtIj42AFVQFwI0BN7i4gWNu9ZGcgE-tdx6dbKzvrORIVB9AEyjjdTDkKG4StslIvz8wkHiTiEKORptbXB54/s1600/computer_screen_programming.png" alt="Implementation" width="30%"/>
</p>

Your main task involves working with the `assignment.py` file using the marimo notebook interface. You need to implement four key functions:

1. **`random_vaccination_strategy(g, num_vaccines)`** - Select nodes randomly for vaccination
2. **`degree_based_vaccination_strategy(g, num_vaccines)`** - Target highest-degree nodes for vaccination  
3. **`calculate_transmission_routes_removed(g, vaccinated_nodes)`** - Calculate total transmission routes removed by vaccination
4. **`evaluate_vaccination_strategy(g, strategy_func, ...)`** - Evaluate strategies using the 1.5x improvement benchmark

Each function includes detailed docstrings with examples and implementation hints. The interactive dashboard lets you test your implementations and compare strategies in real-time on different network types.

### Task 2: Quiz Creation (30 points)

<p align="center">
  <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlHKrBdBIO7hyuXygw_c4F1vwztHkr9cu9Rssl8c6SDEMBAJzYxsJe2IJsDqgLKU6Qx7GJRBlYqI0zvpbD_LdDbCbux_L3GSjQGX6PhHSYv8nf7-QdO4yjVMTQZr25TfnAwRnOt7NG9l4/s180-c/samurai_kettou.png" alt="Quiz Dojo" width="30%"/>
</p>

Create a `quiz.toml` file with exactly five challenging questions about vaccination strategies and transmission route removal in networks. Your quiz will be evaluated by a large language model - craft questions that require deep understanding of network immunization!

**Required format for quiz.toml:**
```toml
[[questions]]
question = "Why is degree-based vaccination more effective than random vaccination?"
answer = "Complete and accurate explanation of the concept."

[[questions]]
question = "Your second challenging question?"
answer = "Complete and accurate answer."

# ... three more questions
```

**Focus areas for questions:**
- Vaccination strategy effectiveness in removing transmission routes
- Calculation and interpretation of transmission routes removed
- Network structure influence on immunization strategy performance
- Improvement factor thresholds and success criteria
- Acquaintance immunization and friendship paradox applications

## Interactive Features

The assignment includes a vaccination strategy comparison dashboard that lets you:
- Test implementations on different network types (scale-free, random, small-world, regular)
- Compare vaccination strategies across network models
- Visualize epidemic time series and vaccination effectiveness
- Explore how network structure affects strategy performance

## Testing Your Implementation

Each function has comprehensive tests checking:
- Correctness on canonical examples (star graphs, complete graphs)
- Strategy comparison and effectiveness validation
- Epidemic simulation properties (SIR state conservation, monotonicity)
- Statistical behavior across multiple simulation runs

## Common Implementation Tips

1. **Random vaccination**: Use `np.random.choice()` with `replace=False`
2. **Degree-based vaccination**: Use `np.argsort()[::-1]` to get highest-degree nodes
3. **Epidemic simulation**: Track node states (S=0, I=1, R=2), simulate transmission along edges
4. **Strategy evaluation**: Run multiple simulations, compute statistical summaries

## Submission Process

1. Implement all four functions in `assignment.py`
2. Create `quiz.toml` with five challenging questions
3. Test using the interactive dashboard
4. Submit via `git add`, `git commit`, `git push`
5. Check autograding results in GitHub Actions

## Grading Criteria

- **Function correctness (70%)**: All implementations pass comprehensive test suites
- **Quiz quality (30%)**: Challenging, accurate questions about network epidemiology
- **Code quality**: Clean, efficient implementations following best practices

## Academic Integrity

- Write your own implementations
- You may discuss concepts but not share code
- Cite any external resources used
- AI assistance must be acknowledged in comments

## Resources

- Course lecture notes on node degree and network epidemiology
- Interactive vaccination games for concept exploration
- Network science literature on epidemic control and targeted interventions
- Public health research on vaccination strategies

---

**Need Help?** Check the course discussion forum or attend office hours. For technical issues, create an issue in this repository.