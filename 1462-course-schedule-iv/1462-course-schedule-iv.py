class Solution:
    # Time = O(n^3)
    # Space = O(n^2)
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        table = [[False for j in range(n)] for i in range(n)]
        
        # Base case: no intermediate vertices
        for row in range(n):
            table[row][row] = False
        for (u, v) in prerequisites:
            table[u][v] = True
            
        # General case: intermediate vertices
        for i in range(n):
            for row in range(n):
                for col in range(n):
                    # Either we have a direct path or 
                    # there's an intermediate vertex in between
                    table[row][col] = table[row][col] or (table[row][i] and table[i][col])
        
        res = []
        for (pre, course) in queries:
            res.append(table[pre][course])
        return res