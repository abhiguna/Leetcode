class Solution:
    
    # Time = O(N)
    # Space = O(1)
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        
        # Set max_product to the max value in the list
        max_product = max(nums)
        
        # Keep track of curr_max and curr_min in the given list
        curr_max = 1
        curr_min = 1
        
        for i in range(N):
            # Store curr_max before updating
            temp = curr_max
            
            # Update curr_max and curr_min
            curr_max = max(nums[i], curr_min * nums[i], curr_max * nums[i])
            curr_min = min(nums[i], curr_min * nums[i], temp * nums[i])
            
            # Update max_product
            max_product = max(max_product, curr_max, curr_min)
        
        return max_product