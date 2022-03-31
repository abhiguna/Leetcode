from collections import *

class Solution:
    
    # Time = O(N)
    # Space = O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        left_product = defaultdict(int)
        left_product[-1] = 1
        
        right_product = defaultdict(int)
        right_product[N] = 1
        
        # Compute the left and right product
        curr_product = 1
        for i in range(N):
            curr_product *= nums[i]
            left_product[i] = curr_product
        
        curr_product = 1
        for i in range(N - 1, -1, -1):
            curr_product *= nums[i]
            right_product[i] = curr_product
        
        res = []
        # Compute the result array
        for i in range(N):
            res.append(left_product[i-1] * right_product[i+1])
        
        return res