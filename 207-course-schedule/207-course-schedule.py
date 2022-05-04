class Solution:
    # Time = O(M + N)
    # Space = O(M + N)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        N = numCourses
        adj_list = [[] for _ in range(N)]
        
        def build_graph():
            for (course, pre) in prerequisites:
                adj_list[pre].append(course)
            return
        
        build_graph()
        
        visited = [-1] * N
        arrival = [-1] * N
        departure = [-1] * N
        timestamp = 0
        
        def dfs(src):
            nonlocal timestamp
            
            visited[src] = 1
            arrival[src] = timestamp
            timestamp += 1
            
            for neighbor in adj_list[src]:
                if visited[neighbor] == -1:
                    has_cycle = dfs(neighbor)
                    if has_cycle:
                        return True
                # Back edge
                elif departure[neighbor] == -1:
                    return True
            
            departure[src] = timestamp
            timestamp += 1
            return False
                
        
        for v in range(N):
            if visited[v] == -1:
                has_cycle = dfs(v)
                if has_cycle:
                    return False
        return True
            