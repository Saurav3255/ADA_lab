
"""
Program: Shortest Path using Dijkstra's and Bellman-Ford Algorithms
Author: Saurav 241492

Description:
Implements Dijkstra's and Bellman-Ford algorithms to find shortest
distances from a source vertex in a weighted directed graph.

Input: Number of vertices, weighted edges, and source vertex.
Output: Shortest distance array or negative cycle error status.
"""

from typing import List
import heapq


class ShortestPath:
    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges = []
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append((u, v, weight))
        self.adj[u].append((v, weight))

    # Dijkstra's Algorithm
    def dijkstra(self, src: int) -> List[int]:
        if not 0 <= src < self.vertices:
            raise ValueError("Invalid source vertex.")

        if any(weight < 0 for _, _, weight in self.edges):
            raise ValueError("Dijkstra's algorithm requires non-negative weights.")

        dist = [float("inf")] * self.vertices
        dist[src] = 0
        pq = [(0, src)]

        while pq:
            current_dist, u = heapq.heappop(pq)

            if current_dist > dist[u]:
                continue

            for v, weight in self.adj[u]:
                new_dist = current_dist + weight

                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        return [int(d) if d != float("inf") else -1 for d in dist]

    # Bellman-Ford Algorithm
    def bellman_ford(self, src: int) -> List[int]:
        if not 0 <= src < self.vertices:
            raise ValueError("Invalid source vertex.")

        dist = [float("inf")] * self.vertices
        dist[src] = 0

        # Relax all edges V-1 times
        for _ in range(self.vertices - 1):
            changed = False

            for u, v, weight in self.edges:
                if dist[u] != float("inf") and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    changed = True

            if not changed:
                break

        # Check for a reachable negative-weight cycle
        for u, v, weight in self.edges:
            if dist[u] != float("inf") and dist[u] + weight < dist[v]:
                raise ValueError("Negative-weight cycle detected.")

        return [int(d) if d != float("inf") else -1 for d in dist]


# Main program
if __name__ == "__main__":
    graph = ShortestPath(5)

    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 1)
    graph.add_edge(2, 1, 2)
    graph.add_edge(1, 3, 1)
    graph.add_edge(2, 3, 5)
    graph.add_edge(3, 4, 3)

    source = 0

    print("Dijkstra's Distances:", graph.dijkstra(source))
    print("Bellman-Ford Distances:", graph.bellman_ford(source))