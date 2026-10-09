
"""
Program: Minimum Spanning Tree using Kruskal's and Prim's Algorithms
Author: Saurav 241492

Description:
Implements Kruskal's and Prim's algorithms to find the Minimum
Spanning Tree of a weighted, undirected graph.

Input: Number of vertices and weighted edges.
Output: MST edge set and total minimum cost.
"""

from typing import List, Tuple
import heapq

Edge = Tuple[int, int, int]  # (source, destination, weight)


class Graph:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges: List[Edge] = []
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append((u, v, weight))
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    # Kruskal's Algorithm
    def kruskal_mst(self) -> List[Edge]:
        parent = list(range(self.vertices))
        rank = [0] * self.vertices

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

            return True

        mst = []

        for u, v, weight in sorted(self.edges, key=lambda edge: edge[2]):
            if union(u, v):
                mst.append((u, v, weight))

                if len(mst) == self.vertices - 1:
                    break

        if len(mst) != self.vertices - 1 and self.vertices > 0:
            raise ValueError("Graph is disconnected; MST does not exist.")

        return mst

    # Prim's Algorithm
    def prim_mst(self) -> List[Edge]:
        if self.vertices == 0:
            return []

        visited = set()
        mst = []
        min_heap = [(0, -1, 0)]  # (weight, parent, vertex)

        while min_heap and len(visited) < self.vertices:
            weight, parent, vertex = heapq.heappop(min_heap)

            if vertex in visited:
                continue

            visited.add(vertex)

            if parent != -1:
                mst.append((parent, vertex, weight))

            for neighbor, edge_weight in self.adj[vertex]:
                if neighbor not in visited:
                    heapq.heappush(
                        min_heap, (edge_weight, vertex, neighbor)
                    )

        if len(mst) != self.vertices - 1:
            raise ValueError("Graph is disconnected; MST does not exist.")

        return mst


# Main program
if __name__ == "__main__":
    graph = Graph(5)

    graph.add_edge(0, 1, 2)
    graph.add_edge(0, 3, 6)
    graph.add_edge(1, 2, 3)
    graph.add_edge(1, 3, 8)
    graph.add_edge(1, 4, 5)
    graph.add_edge(2, 4, 7)
    graph.add_edge(3, 4, 9)

    # Kruskal's MST
    kruskal_edges = graph.kruskal_mst()
    print("Kruskal's MST:", kruskal_edges)
    print("Kruskal's Minimum Cost:", sum(e[2] for e in kruskal_edges))

    # Prim's MST
    prim_edges = graph.prim_mst()
    print("\nPrim's MST:", prim_edges)
    print("Prim's Minimum Cost:", sum(e[2] for e in prim_edges))