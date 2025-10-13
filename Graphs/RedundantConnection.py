class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx == rooty:
                return False
            
            if rank[rootx] > rank[rooty]:
                parent[rooty] = rootx
                rank[rootx] += rank[rooty]
            
            else:
                parent[rootx] = rooty
                rank[rooty] += rank[rootx]
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a,b]

