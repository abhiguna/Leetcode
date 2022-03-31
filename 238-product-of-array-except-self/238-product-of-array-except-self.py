class Solution:
    
    # Time = O(N)
    # Space = O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)

        res = []
        # Compute the left product of the res array
        curr_prod = 1
        for i in range(N):
            res.append(curr_prod)
            curr_prod *= nums[i]
        
        # Update result array by multiplying with the right product
        curr_prod = 1
        for i in range(N-1, -1, -1):
            res[i] *= curr_prod
            curr_prod *= nums[i]
        
        return res