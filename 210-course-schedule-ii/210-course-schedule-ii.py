class Solution:
    # Time = O(n + m), n: numCourses, m: len(prerequisites)
    # Space = O(n + m)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]
        in_deg = {c: 0 for c in range(numCourses)}
        
        # Build the graph
        for (course, pre) in prerequisites:
            adj_list[pre].append(course)
            in_deg[course] += 1
        
        topsort = []
        
        # Kahn's topological sort algorithm
        queue = deque()
        for (c, deg) in in_deg.items():
            if deg == 0:
                topsort.append(c)
                queue.append(c)
        
        while queue:
            curr_course = queue.popleft()
            
            for ncourse in adj_list[curr_course]:
                in_deg[ncourse] -= 1
                if in_deg[ncourse] == 0:
                    topsort.append(ncourse)
                    queue.append(ncourse)
        
        # Check cycle
        if len(topsort) < numCourses:
            return []
        
        return topsort