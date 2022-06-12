class Solution:
    # Time = O(m+n)
    # Space = O(m+n)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m, n = len(prerequisites), numCourses
        
        adj_list = [[] for v in range(n)]
        in_deg = {v: 0 for v in range(n)}
        ordering = []
        
        # Build adj_list and in_deg
        for (course, prereq) in prerequisites:
            adj_list[prereq].append(course)
            in_deg[course] += 1
        
        queue = deque()
        for (key, val) in in_deg.items():
            if val == 0:
                queue.append(key)
        
        while queue:
            course = queue.popleft()
            ordering.append(course)
            
            for nei in adj_list[course]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    queue.append(nei)
        
        if len(ordering) < n:
            return []
        
        return ordering