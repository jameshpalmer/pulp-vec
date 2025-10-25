"""
Basic usage example for pulp-vec

This example demonstrates:
1. Creating a simple LP problem with DecisionSeries
2. Adding constraints using vectorized operations
3. Solving with the HiGHS solver
"""

from pulp_vec import DecisionSeries, LpProblem

# Create a maximization problem
prob = LpProblem("BasicExample", sense=1)  # 1 = maximize

# Create decision variables 'a' indexed from 0 to 4
a = DecisionSeries.lp_variable("a", range(5), model=prob)
print("Decision variables a:")
print(a)
print()

# Create decision variables 'b' indexed from 3 to 8
b = DecisionSeries.lp_variable("b", range(6), model=prob)
b.index += 3  # Shift index to start at 3
print("Decision variables b:")
print(b)
print()

# Add constraint: a <= b (vectorized operation across overlapping indices)
prob += a <= b
print("Problem with constraint a <= b:")
print(prob)
print()

# Demonstrate arithmetic operations
c = 1 - a  # Vectorized subtraction
print("Result of 1 - a:")
print(c)
print()

# Set an objective function: maximize sum of a
prob.model += a.sum()

# Solve the problem
status = prob.solve()
print(f"Solution status: {status}")
print()

# Get the solution values
if status == 1:  # 1 = optimal solution found
    solution = a.get_value()
    print("Solution values for a:")
    print(solution)
