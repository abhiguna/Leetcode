class Solution:
    # Time = O(M + N), M: len(prerequisites), N: numCourses
    # Space = O(M + N)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for i in range(numCourses)]
        arrival = [-1] * numCourses
        departure = [-1] * numCourses
        timestamp = [0]
        
        def build_graph():
            for (c, pre) in prerequisites:
                adj_list[pre].append(c)
            return
        
        def dfs(src):
            arrival[src] = timestamp[0]
            timestamp[0] += 1
            
            for nei in adj_list[src]:
                if arrival[nei] == -1:
                    has_cycle = dfs(nei)
                    if has_cycle:
                        return True
                else:
                    # backedge
                    if departure[nei] == -1:
                        return True
            
            departure[src] = timestamp[0]
            timestamp[0] += 1
            return False
        
        build_graph()
        
        for v in range(numCourses):
            if arrival[v] == -1:
                has_cycle = dfs(v)
                if has_cycle:
                    return False
        
        return True