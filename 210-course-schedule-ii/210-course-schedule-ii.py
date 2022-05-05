from collections import *

class Solution:
    # Time = O(M + N)
    # Space = O(M + N)
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        N = numCourses
        M = len(prerequisites)
        adj_list = [[] for _ in range(N)]
        in_deg = defaultdict(int)
        
        def build_graph():
            for (c, pre) in prerequisites:
                adj_list[pre].append(c)
                in_deg[c] += 1
            return
        
        
        build_graph()
        bag = deque()
        for c in range(N):
            if in_deg[c] == 0:
                bag.append(c)
        
        course_list = []
        while bag:
            curr = bag.popleft()
            course_list.append(curr)
            
            for neighbor in adj_list[curr]:
                in_deg[neighbor] -= 1
                if in_deg[neighbor] == 0:
                    bag.append(neighbor)
        
        if len(course_list) < N:
            return []
        
        return course_list
                
        