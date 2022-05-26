class Solution:
    # Time = O(N)
    # Space = O(1)
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = 0
        window_product = 1
        left = 0
        
        # Variable size sliding window
        for i in range(N):
            window_product *= nums[i]
            
            while left <= i and window_product >= k:
                window_product /= nums[left]
                left += 1
            
            count += (i - left + 1)
        
        return count