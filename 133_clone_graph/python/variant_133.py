"""
# Definition for a Node.
"""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Graph:
    def __init__(self, roots: list[Node] = []):
        self.roots = roots


class Solution:
    def cloneGraph(self, graph: Graph) -> Graph:
        output_roots = []

        def cloneConnectedGraph(node: Optional["Node"]):
            if not node:
                return node

            visited = {}

            def dfs(node: Optional["Node"]) -> Optional["Node"]:
                nonlocal visited
                if not node:
                    return node  # If node is undefined

                if node in visited:
                    # If visited already, return existing clone
                    return visited[node]

                clone_node = Node(node.val, [])  # Make a copy
                # Add entry to visited map
                visited[node] = clone_node
                # Run cloneGraph recursively
                if node.neighbors:
                    clone_node.neighbors = [dfs(n) for n in node.neighbors]
                return clone_node

            return dfs(node)

        output_roots = [
            cloneConnectedGraph(root) for root in graph.roots if root is not None
        ]
        return Graph(roots=output_roots)
