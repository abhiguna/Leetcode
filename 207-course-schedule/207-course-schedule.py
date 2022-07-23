class Solution:
    # Time = O(m+n), m: len(prerequisites), n: numCourses
    # Space = O(m+n)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for v in range(numCourses)]
        arrival = [-1] * numCourses
        departure = [-1] * numCourses
        timestamp = [0]
        
        # Build the graph
        def build_graph():
            for (course, pre) in prerequisites:
                adj_list[pre].append(course)
            
        
        build_graph()
        
        # DFS -> return whether cycle exists
        def dfs(node):
            arrival[node] = timestamp[0]
            timestamp[0] += 1
            
            for nei in adj_list[node]:
                if arrival[nei] == -1:
                    has_cycle = dfs(nei)
                    if has_cycle:
                        return True
                else:
                    # Back edge 
                    if departure[nei] == -1:
                        return True
            
            departure[node] = timestamp[0]
            timestamp[0] += 1
            return False
            
        
        # Outer loop -> traverse all components
        for v in range(numCourses):
            if arrival[v] == -1:
                has_cycle = dfs(v)
                if has_cycle:
                    return False
        
        return True