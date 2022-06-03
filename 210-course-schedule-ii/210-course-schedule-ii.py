class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for i in range(numCourses)]
        arrival = [-1] * numCourses
        departure = [-1] * numCourses
        timestamp = [0]
        # A valid course schedule will have decreasing order of departure times
        topsort = []
        
        def build_graph():
            for (a, b) in prerequisites:
                adj_list[b].append(a)
            return
        
        def dfs(node):
            arrival[node] = timestamp[0]
            timestamp[0] += 1
            
            for nei in adj_list[node]:
                # Neighbor not visited
                if arrival[nei] == -1:
                    has_cycle = dfs(nei)
                    if has_cycle:
                        return True
                else:
                    # Found back edge -> cycle
                    if departure[nei] == -1:
                        return True
            
            departure[node] = timestamp[0]
            timestamp[0] += 1
            topsort.append(node)
            return False
                    
        
        
        
        # Build a dir graph
        build_graph()
        
        for v in range(numCourses):
            if arrival[v] == -1:
                has_cycle = dfs(v)
                if has_cycle:
                    return []
        
        topsort.reverse() # Topsort contains elements in increasing order of departure times, so we need to reverse it before returning it
        return topsort
        
        
                
        