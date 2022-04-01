class Solution:
    
    # Time = O(N)
    # Space = O(1)
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        
        # Stores the max value in nums
        res = max(nums)
        
        # Keep track of the curr_max and curr_min of subarray ending at idx i
        curr_max = 1
        curr_min = 1
        
        for i in range(N):
            temp = nums[i] * curr_max
            
            # Update curr_max and curr_min
            curr_max = max(nums[i], nums[i] * curr_max, nums[i] * curr_min)
            curr_min = min(nums[i], temp, nums[i] * curr_min)
            
            # Update res
            res = max(res, curr_max, curr_min)
        
        return res