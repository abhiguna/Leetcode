class Solution:
    # Time = O(N + M)
    # Space = O(N + M)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        N = numCourses
        M = len(prerequisites)
        
        adj_list = [[] for _ in range(N)]
        arrival = [-1] * N
        departure = [-1] * N
        timestamp = [0]
        
        def build_graph():
            for crs, pre in prerequisites:
                adj_list[pre].append(crs)
            return
        
        def dfs(src):
            arrival[src] = timestamp[0]
            timestamp[0] += 1
            
            for neighbor in adj_list[src]:
                if arrival[neighbor] == -1:
                    has_cycle = dfs(neighbor)
                    if has_cycle: return True
                else:
                    # Check back edge
                    if departure[neighbor] == -1:
                        return True # hasCycle
            
            departure[src] = timestamp[0]
            timestamp[0] += 1
            return False
            
        build_graph()
        for c in range(numCourses):
            has_cycle = dfs(c)
            if has_cycle: return False
        
        return True