class Solution:
    # Time = O(m+n), n: # of courses, m: len(relations)
    # Space = O(m+n)
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # Topological sort
        adj_list = [[] for v in range(n+1)]
        in_deg = {v:0 for v in range(1, n+1)}
        
        def build_graph():
            for (pre, course) in relations:
                adj_list[pre].append(course)
                in_deg[course] += 1
        
        # Build the graph
        build_graph()
        
        queue = deque()
        # Insert all the nodes with an in-deg of 0
        for (v, deg) in in_deg.items():
            if deg == 0:
                queue.append((v, 1))
        
        min_sem = 0
        num_nodes = 0
        
        while queue:
            (node, sem_num) = queue.popleft()
            num_nodes += 1
            min_sem = max(min_sem, sem_num)
            
            for nei in adj_list[node]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    queue.append((nei, sem_num + 1))
        
        # Check for cyclical dependency
        if num_nodes < n:
            return -1
        
        return min_sem
        
        
                
            