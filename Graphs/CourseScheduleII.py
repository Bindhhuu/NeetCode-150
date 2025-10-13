class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        unvisited = 0
        visited = 2
        visiting = 1
        states = [unvisited]* numCourses

        def dfs(i):
            if states[i] == visiting:
                return False
            elif states[i] == visited:
                return True
            states[i] = visiting

            for nei in g[i]:
                if not dfs(nei):
                    return False

            states[i] = visited
            order.append(i) 
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return order
