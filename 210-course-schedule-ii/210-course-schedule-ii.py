class Solution:
    # Time = O(m+n), m: len(prerequisites), n: numCourses
    # Space = O(m+n)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for v in range(numCourses)]
        in_deg = {v: 0 for v in range(numCourses)}
        
        def build_graph():
            for (course, pre) in prerequisites:
                adj_list[pre].append(course)
                in_deg[course] += 1
        
        # Build graph
        build_graph()
        
        # Kahn's topological sorting algo.
        res = []
        queue = deque()
        
        for (course, num_pre) in in_deg.items():
            if num_pre == 0:
                res.append(course)
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            
            for ncourse in adj_list[course]:
                in_deg[ncourse] -= 1
                if in_deg[ncourse] == 0:
                    queue.append(ncourse)
                    res.append(ncourse)
        
        # Check for cycle
        if len(res) < numCourses:
            return []
        
        return res
        