class Solution:
    # Approach: Memoization
    
    # Time = O(N*half_total)
    # Space = O(N*half_total)
    def canPartition(self, nums: List[int]) -> bool:
        # Edge case
        if sum(nums) % 2 != 0:
            return False
        
        memo = {}
        N = len(nums)
        total = sum(nums)
        half_total = total // 2
        memo[(0, 0)] = True
        
        # Base cases
        # Fill first row
        for val in range(1, half_total + 1):
            memo[(0, val)] = False
            
        # Fill first col
        for size in range(1, N+1):
            memo[(size, 0)] = True
        
        def helper(size, target):
            if (size, target) in memo:
                return memo[(size, target)]
            
            # Include curr element
            if target - nums[size-1] >= 0:
                memo[(size, target)] = helper(size - 1, target - nums[size-1]) or helper(size-1, target)
            # Exclude curr element
            else:
                memo[(size, target)] = helper(size-1, target)
            
            return memo[(size, target)]
        
        return helper(N, half_total)
            