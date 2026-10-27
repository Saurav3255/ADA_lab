
"""
Program: Graph Backtracking Algorithms
Author: Saurav 241492

Description:
Implements graph coloring and Hamiltonian cycle detection
using backtracking.

Input: An adjacency matrix and the number of available colors.
Output: A vertex-color mapping and a Hamiltonian cycle, if found.
"""

from typing import List


class GraphBacktracker:
    def __init__(self, graph: List[List[int]]):
        n = len(graph)

        if any(len(row) != n for row in graph):
            raise ValueError("Graph must be a square adjacency matrix.")

        self.graph = graph
        self.n = n

    def graph_coloring(self, m: int) -> List[int]:
        """Return a valid color assignment, or [] if none exists."""
        if m < 1 and self.n > 0:
            return []

        colors = [0] * self.n

        def is_safe(vertex: int, color: int) -> bool:
            for neighbor in range(self.n):
                if (
                    self.graph[vertex][neighbor]
                    and colors[neighbor] == color
                ):
                    return False
            return True

        def backtrack(vertex: int) -> bool:
            if vertex == self.n:
                return True

            for color in range(1, m + 1):
                if is_safe(vertex, color):
                    colors[vertex] = color

                    if backtrack(vertex + 1):
                        return True

                    colors[vertex] = 0

            return False

        if backtrack(0):
            return colors

        return []

    def hamiltonian_cycle(self) -> List[int]:
        """Return a Hamiltonian cycle, or [] if none exists."""
        if self.n == 0:
            return []

        path = [0] * self.n
        path[0] = 0

        def is_safe(vertex: int, position: int) -> bool:
            # Must connect to the previous vertex.
            if not self.graph[path[position - 1]][vertex]:
                return False

            # A vertex cannot appear twice in the path.
            if vertex in path[:position]:
                return False

            return True

        def backtrack(position: int) -> bool:
            if position == self.n:
                # Last vertex must connect to the starting vertex.
                return bool(self.graph[path[-1]][path[0]])

            for vertex in range(1, self.n):
                if is_safe(vertex, position):
                    path[position] = vertex

                    if backtrack(position + 1):
                        return True

                    path[position] = 0

            return False

        if self.n == 1:
            return [0, 0] if self.graph[0][0] else []

        if backtrack(1):
            return path + [path[0]]

        return []


# Main program
if __name__ == "__main__":
    graph = [
        [0, 1, 1, 1],
        [1, 0, 1, 0],
        [1, 1, 0, 1],
        [1, 0, 1, 0]
    ]

    solver = GraphBacktracker(graph)

    print("Graph Coloring (3 colors):")
    coloring = solver.graph_coloring(3)
    print(coloring if coloring else "No valid coloring exists.")

    print("\nHamiltonian Cycle:")
    cycle = solver.hamiltonian_cycle()
    print(cycle if cycle else "No Hamiltonian cycle exists.")
