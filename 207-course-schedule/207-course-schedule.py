class Solution:
    # Time = O(M+N), M: len(prereqs), N: numCourses
    # Space = O(M+N)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Cycle detection
        adj_list = [[] for i in range(numCourses)]
        arrival = [-1] * numCourses
        departure = [-1] * numCourses
        timestamp = [0]
        
        def build_graph():
            for (a, b) in prerequisites:
                adj_list[b].append(a)
            return
        
        # Builds dir. graph from prereqs
        build_graph()
        
        def dfs(node):
            arrival[node] = timestamp[0]
            timestamp[0] += 1
            
            for nei in adj_list[node]:
                if arrival[nei] == -1:
                    has_cycle = dfs(nei)
                    if has_cycle: 
                        return True
                else:
                    if departure[nei] == -1:
                        # Found a back edge -> cycle
                        return True
            
            departure[node] = timestamp[0]
            timestamp[0] += 1
            return False
        
        
        # Outer loop
        for v in range(numCourses):
            if arrival[v] == -1:
                has_cycle = dfs(v)
                if has_cycle:
                    return False
        
        return True