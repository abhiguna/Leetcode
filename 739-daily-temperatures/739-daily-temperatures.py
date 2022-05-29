class Solution:
    # Time = O(N)
    # Space = O(N)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        stack = deque() # Stack contains (temperature, day)
        res = []
        
        for i in range(N-1, -1, -1):
            while stack and stack[-1][0] <= temperatures[i]:
                stack.pop()
            
            # If stack not empty -> find the difference in days
            if stack:
                res.append(stack[-1][1] - i)
            
            # If stack is empty -> add 0
            else:
                res.append(0)
            
            # Push the current day
            stack.append((temperatures[i], i))
        
        res.reverse()
        return res