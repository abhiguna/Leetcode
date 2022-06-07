class Solution:
    # Check if topsort if possible
    # Time = O(M+N)
    # Space = O(M+N)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the in-degree of each node
        in_deg = {v:0 for v in range(numCourses)}
        adj_list = [[] for v in range(numCourses)]
        
        for (c, pre) in prerequisites:
            adj_list[pre].append(c)
            in_deg[c] += 1
        
        # Add all the nodes with in-deg of 0 to a queue
        queue = deque()
        for c in in_deg:
            if in_deg[c] == 0:
                queue.append(c)
        
        topsort = []
        while queue:
            node = queue.popleft()
            topsort.append(node)
            
            for nei in adj_list[node]:
                # if nei in in_deg:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    queue.append(nei)
        
        if len(topsort) < numCourses:
            return False

        return True
            
        
        
        
        
        