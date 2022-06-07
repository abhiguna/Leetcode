class Solution:
    # Time = O(N)
    # Space = O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N
        
        # Fill prefix product
        prefix_prod = 1
        for i in range(0, N):
            res[i] = prefix_prod
            prefix_prod = prefix_prod * nums[i]
            
        # Multiply suffix product
        suffix_prod = 1
        for i in range(N-1, -1, -1):
            res[i] = res[i] * suffix_prod
            suffix_prod = suffix_prod * nums[i]
        
        return res