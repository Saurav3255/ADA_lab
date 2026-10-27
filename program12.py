
"""
Program: Floyd-Warshall and Optimal BST
Author: Saurav 241492

Description:
Implements the Floyd-Warshall algorithm to find all-pairs
shortest paths and Optimal BST to calculate minimum search cost.

Input: A distance matrix for Floyd-Warshall and sorted keys
       with their frequencies for Optimal BST.
Output: Shortest-path distance matrix and minimum BST search cost.
"""

from typing import List


def floyd_warshall(graph: List[List[int]]) -> List[List[int]]:
    n = len(graph)

    if any(len(row) != n for row in graph):
        raise ValueError("Graph must be a square matrix.")

    # Copy the graph so the original matrix remains unchanged.
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float("inf") and dist[k][j] != float("inf"):
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

    # A negative diagonal value indicates a negative cycle.
    if any(dist[i][i] < 0 for i in range(n)):
        raise ValueError("Graph contains a negative-weight cycle.")

    return dist


def optimal_bst(keys: List[int], freq: List[int]) -> int:
    if len(keys) != len(freq):
        raise ValueError("Keys and frequencies must have equal lengths.")

    if any(freq[i] < 0 for i in range(len(freq))):
        raise ValueError("Frequencies cannot be negative.")

    if any(keys[i] >= keys[i + 1] for i in range(len(keys) - 1)):
        raise ValueError("Keys must be sorted in strictly increasing order.")

    n = len(keys)

    if n == 0:
        return 0

    # cost[i][j] stores minimum search cost for keys i through j.
    cost = [[0] * n for _ in range(n)]

    # Prefix sums allow efficient frequency-sum calculation.
    prefix = [0]
    for f in freq:
        prefix.append(prefix[-1] + f)

    for i in range(n):
        cost[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total_freq = prefix[j + 1] - prefix[i]
            cost[i][j] = float("inf")

            for root in range(i, j + 1):
                left = cost[i][root - 1] if root > i else 0
                right = cost[root + 1][j] if root < j else 0

                current_cost = left + right + total_freq
                cost[i][j] = min(cost[i][j], current_cost)

    return cost[0][n - 1]


# Main program
if __name__ == "__main__":
    INF = float("inf")

    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]

    print("Floyd-Warshall Shortest Path Matrix:")
    for row in floyd_warshall(graph):
        print([("INF" if x == INF else x) for x in row])

    keys = [10, 20, 30]
    freq = [34, 8, 50]

    print("\nOptimal BST Minimum Search Cost:")
    print(optimal_bst(keys, freq))
