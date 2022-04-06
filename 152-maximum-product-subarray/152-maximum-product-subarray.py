class Solution:
    
    # Time = O(N)
    # Space = O(1)
    def maxProduct(self, nums: List[int]) -> int:
        max_product = max(nums)
        curr_max = 1
        curr_min = 1
        
        for num in nums:
            temp = curr_max
            curr_max = max(num, temp * num, curr_min * num)
            curr_min = min(num, temp * num, curr_min * num)
            
            max_product = max(max_product, curr_max, curr_min)
        
        return max_product