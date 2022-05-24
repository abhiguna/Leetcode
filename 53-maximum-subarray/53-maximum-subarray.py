class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        
        # Maintain the global maximum sum as well as the current maximum ending at the curr idx i
        global_max = nums[0]
        curr_max = nums[0]
        for i in range(1, N):
            # Update curr max as well as the global max
            # curr max will either extend the curr max at the prev idx or will be equal to the value of 
            #.  the current element
            curr_max = max(curr_max + nums[i], nums[i])
            global_max = max(global_max, curr_max)
        
        return global_max