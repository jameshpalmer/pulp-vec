# pulp-vec

Vector-based utilities for PuLP - numpy-compatible wrappers for large-scale linear programming.

## Overview

`pulp-vec` provides numpy-style wrapper classes for [PuLP](https://github.com/coin-or/pulp) to enable vectorized operations on decision variables. This makes it much easier to work with large-scale Mixed Integer Linear Programming (MILP) problems by allowing you to manipulate decision variables using familiar numpy patterns.

## Key Features

- **`LpProblem`**: Enhanced wrapper around PuLP's LpProblem with cleaner syntax
- **`DecisionSeries`**: 1D array-like structure for decision variables with full arithmetic support
- **`DecisionMatrix`**: 2D array-like structure for decision variables
- **Vectorized operations**: Add, subtract, multiply decision variables across indices
- **Automatic constraint generation**: Use comparison operators (`<=`, `>=`, `==`) to generate constraints
- **Index alignment**: Operations on mismatched indices automatically handle overlaps

## Installation

```bash
pip install pulp-vec
```

Or with uv:

```bash
uv add pulp-vec
```

## Quick Start

```python
from pulp_vec import LpProblem, DecisionSeries

# Create a problem
prob = LpProblem("Example", sense=1)  # 1 = maximize

# Create decision variables indexed 0-4
x = DecisionSeries.lp_variable("x", range(5), model=prob)

# Create more decision variables indexed 3-8
y = DecisionSeries.lp_variable("y", range(6), model=prob)
y.index += 3

# Add constraints using vectorized operations
prob += x <= y  # Only applies to overlapping indices (3, 4)
prob += x >= 0

# Set objective and solve
prob.model += x.sum()
prob.solve()

# Get solution
solution = x.get_value()
print(solution)
```

## Why pulp-vec?

When building large optimization models, you often need to:

1. Create hundreds or thousands of decision variables
2. Apply similar constraints across many variables
3. Work with structured data (like time series or matrices)

Standard PuLP requires loops and manual index management. `pulp-vec` lets you work with decision variables the same way you work with numpy arrays.

### Standard PuLP approach:
```python
# Create 100 variables manually
x = {}
for i in range(100):
    x[i] = pulp.LpVariable(f"x_{i}", lowBound=0)

# Add constraints in a loop
for i in range(100):
    if i in y:
        prob += x[i] <= y[i]
```

### pulp-vec approach:
```python
# Create 100 variables at once
x = DecisionSeries.lp_variable("x", range(100), low_bound=0, model=prob)

# Add constraints vectorized (automatically handles index matching)
prob += x <= y
```

## Examples

See the [`examples/`](examples/) directory for more detailed examples:

- `basic_usage.py` - Introduction to DecisionSeries and basic operations

## Documentation

### DecisionSeries

1D array structure for decision variables:

```python
# Create from LP variables
x = DecisionSeries.lp_variable(
    name="x",
    index=range(10),
    low_bound=0,
    up_bound=10,
    cat="Integer",  # or "Binary", "Continuous"
    model=prob
)

# Arithmetic operations
y = 2 * x + 5
z = x - y

# Indexing
x[3]  # Get single element
x[[1, 1, 0, 1, ...]]  # Boolean indexing

# Constraints
prob += x >= 0
prob += x <= 10
prob += x == 5
```

### DecisionMatrix

2D array structure for decision variables:

```python
# Create matrix of decision variables
matrix = DecisionMatrix.lp_variable(
    name="m",
    index=range(5),      # rows
    columns=range(3),     # columns
    model=prob
)

# Column access
col = matrix[0]  # Returns DecisionSeries

# Element access
matrix[2, 1]  # Row 2, column 1

# Operations
matrix2 = matrix * 2
prob += matrix <= 1
```

## Dependencies

- Python ≥ 3.9
- PuLP ≥ 2.7.0
- NumPy ≥ 1.20.0

## License

MIT License - feel free to use in your projects!

## Contributing

Contributions welcome! Please feel free to submit issues or pull requests.

## Related Projects

- [PuLP](https://github.com/coin-or/pulp) - The underlying LP/MILP library
- [HiGHS](https://highs.dev/) - The default solver (free and open-source)
