class Solution:
    # Time = O(m+n), m: len(prerequisites), n: numCourses
    # Space = O(m+n)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for v in range(numCourses)]
        arrival = [-1] * numCourses
        departure = [-1] * numCourses
        timestamp = [0]
        course_list = []
        
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
            
            # Add the course to the course list before departing
            course_list.append(node)
            departure[node] = timestamp[0]
            timestamp[0] += 1
            return False
            
        
        # Outer loop -> traverse all components
        for v in range(numCourses):
            if arrival[v] == -1:
                has_cycle = dfs(v)
                if has_cycle:
                    return []
        
        # Course order must be in decreasing order of departure times
        course_list.reverse()
        return course_list