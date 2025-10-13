"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        start = node
        stack = [start]
        oldtonew = {}
        visited = set()
        visited.add(start)

        while stack:
            node = stack.pop()
            oldtonew[node] = Node(val = node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)

        for old, new in oldtonew.items():
            for nei in old.neighbors:
                newnode = oldtonew[nei]
                new.neighbors.append(newnode)

        return oldtonew[start]

        '''
        if not node:
            return Node
        visited = {}
        def dfs(n):
            if n in visited:
                return visited[n]
            clone = Node(n.val)
            visited[n] = clone
            for nei in neighbors:
                clone.neighbors.append(dfs(nei))
            return clone
        return dfs(node)
        '''
        
