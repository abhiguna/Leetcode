class Solution:
    # Approach: DP
    
    # Time = O(N)
    # Space = O(1)
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        # Edge case
        if N == 1:
            return nums[0]
        
        def rob_linear(loots):
            if len(loots) <= 0:
                return 0
            
            if len(loots) == 1:
                return loots[0]
            
            first = loots[0]
            second = max(loots[0], loots[1])
            
            for h in range(2, len(loots)):
                third = max(second, loots[h] + first)
                first = second
                second = third
            
            return second
        
        # Two cases: rob the first house or not rob it
        return max(nums[0] + rob_linear(nums[2:N-1]), rob_linear(nums[1:N]))
        