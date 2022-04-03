class Solution:
    
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        
        # Keep track of the max_product as well as the curr_max and curr_min
        # product of a previous subarray
        
        max_product = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]
        
        for i in range(1, N):
            temp = curr_max
            curr_max = max(nums[i], curr_min * nums[i], curr_max * nums[i])
            curr_min = min(nums[i], curr_min * nums[i], temp * nums[i])
            
            max_product = max(max_product, curr_max, curr_min)
        
        return max_product