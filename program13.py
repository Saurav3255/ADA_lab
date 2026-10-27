
"""
Program: Travelling Salesperson Problem (TSP)
Author: Saurav 241492

Description:
Implements the TSP using dynamic programming and bitmasking
to find the minimum cost Hamiltonian tour.

Input: A square distance matrix representing cities and travel costs.
Output: Minimum cost of a tour visiting every city and returning
        to the starting city.
"""

from typing import List
from functools import lru_cache


class TSPSolver:
    def solve_tsp(self, dist_matrix: List[List[int]]) -> int:
        n = len(dist_matrix)

        if n == 0:
            return 0

        if any(len(row) != n for row in dist_matrix):
            raise ValueError("Distance matrix must be square.")

        if any(
            dist_matrix[i][j] < 0
            for i in range(n)
            for j in range(n)
            if i != j
        ):
            raise ValueError("Distances cannot be negative.")

        if n == 1:
            return 0

        # INF represents an unavailable route.
        INF = float("inf")
        full_mask = (1 << n) - 1

        @lru_cache(maxsize=None)
        def dp(mask: int, current: int) -> float:
            # All cities visited: return to starting city 0.
            if mask == full_mask:
                return (
                    dist_matrix[current][0]
                    if dist_matrix[current][0] != INF
                    else INF
                )

            min_cost = INF

            for next_city in range(1, n):
                if not (mask & (1 << next_city)):
                    distance = dist_matrix[current][next_city]

                    if distance == INF:
                        continue

                    remaining_cost = dp(
                        mask | (1 << next_city),
                        next_city
                    )

                    if remaining_cost != INF:
                        min_cost = min(
                            min_cost,
                            distance + remaining_cost
                        )

            return min_cost

        result = dp(1, 0)

        if result == INF:
            raise ValueError("No complete tour exists.")

        return int(result)


# Main program
if __name__ == "__main__":
    dist_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    solver = TSPSolver()
    result = solver.solve_tsp(dist_matrix)

    print("Distance Matrix:")
    for row in dist_matrix:
        print(row)

    print("Minimum TSP Tour Cost:", result)
