"""
pulp-vec: Vector-based utilities for PuLP optimization
======================================================

Provides pandas/numpy-compatible wrapper classes for PuLP to enable
vectorized operations on decision variables, making it easier to work
with large-scale linear programming problems.
"""

from pulp_vec.lp_tools import LpProblem, DecisionSeries, DecisionMatrix

__version__ = "0.1.0"
__all__ = ["LpProblem", "DecisionSeries", "DecisionMatrix"]
