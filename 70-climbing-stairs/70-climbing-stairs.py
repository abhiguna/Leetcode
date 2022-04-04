class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        opt = [1] * (n + 1)
        
        for i in range(2, n + 1):
            opt[i] = opt[i-1] + opt[i-2]
        
        return opt[n]