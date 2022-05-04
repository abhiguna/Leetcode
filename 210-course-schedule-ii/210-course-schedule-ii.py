class Solution:
    # --- Kahn's Topological Sort Algorithm
    # Time = O(M + N)
    # Space = O(M + N)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        N = numCourses
        M = len(prerequisites)
        
        adj_list = [[] for _ in range(N)]
        in_degrees = [0] * N
        
        def build_graph():
            for (course, pre) in prerequisites:
                adj_list[pre].append(course)
                in_degrees[course] += 1
            return
        
        build_graph()
        
        # queue <- v with in_deg = 0
        queue = deque()
        for (course, num_pre) in enumerate(in_degrees):
            if num_pre == 0:
                queue.append(course)
        
        course_list = []
        while queue:
            curr = queue.popleft()
            course_list.append(curr)
            
            for neighbor in adj_list[curr]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check for cyclical dependency
        if len(course_list) < N:
            return []
        
        return course_list