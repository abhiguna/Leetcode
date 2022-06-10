class Solution:
    # Time = O(N)
    # Space = O(N)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        mon_stack = []
        res = [0] * N
        
        for i in range(N-1, -1, -1):
            # Remove all the days that have a temperature <= curr temperature
            while mon_stack and mon_stack[-1][0] <= temperatures[i]:
                mon_stack.pop()
            
            if mon_stack:
                res[i] = mon_stack[-1][1] - i
            
            mon_stack.append((temperatures[i], i))
            
        return res