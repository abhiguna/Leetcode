class Solution:
    # Time = O(m+n)
    # Space = O(m+n)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m = len(prerequisites)
        n = numCourses
        
        adj_list = [[] for v in range(n)]
        topsort = []
        arrival = [-1] * n
        departure = [-1] * n
        timestamp = [0]
        
        def build_graph():
            for (c, pre) in prerequisites:
                adj_list[pre].append(c)
            
        # Build the graph
        build_graph()
        
        # DFS
        def dfs(src):
            arrival[src] = timestamp[0]
            timestamp[0] += 1
            
            for nei in adj_list[src]:
                # Tree Edge
                if arrival[nei] == -1:
                    has_cycle = dfs(nei)
                    if has_cycle:
                        return True
                # Back Edge -> cycle exists
                else:
                    if departure[nei] == -1:
                        return True
            
            # Add the node to topsort before departing
            topsort.append(src)
            departure[src] = timestamp[0]
            timestamp[0] += 1
            return False
        
        # Outer loop
        for v in range(n):
            if arrival[v] == -1:
                has_cycle = dfs(v)
                if has_cycle:
                    return []
        
        topsort.reverse() # Must be in decreasing order of departure times
        return topsort