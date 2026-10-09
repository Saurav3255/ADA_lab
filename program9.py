
"""
Program: 0/1 Knapsack using Dynamic Programming
Author: Saurav 241492

Description:
Implements the 0/1 Knapsack problem using 2D and 1D DP methods
to maximize the total value without exceeding the capacity.

Input: List of weights, list of values, and knapsack capacity.
Output: Maximum attainable value as an integer.
"""

from typing import List


# 1. 2D Dynamic Programming
def knapsack_01_2d(weights: List[int], values: List[int],
                    capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]

            if weight <= w:
                dp[i][w] = max(
                    dp[i][w],
                    value + dp[i - 1][w - weight]
                )

    return dp[n][capacity]


# 2. 1D Dynamic Programming (Space Optimized)
def knapsack_01(weights: List[int], values: List[int],
                capacity: int) -> int:
    if len(weights) != len(values):
        raise ValueError("Weights and values must have equal lengths.")
    if capacity < 0 or any(w < 0 for w in weights):
        raise ValueError("Weights and capacity must be non-negative.")

    dp = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], value + dp[w - weight])

    return dp[capacity]


# Main program
if __name__ == "__main__":
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7

    print("2D DP Maximum Value:",
          knapsack_01_2d(weights, values, capacity))

    print("1D DP Maximum Value:",
          knapsack_01(weights, values, capacity))