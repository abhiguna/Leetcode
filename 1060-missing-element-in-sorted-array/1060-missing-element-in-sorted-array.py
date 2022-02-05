class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return nums[0] + k
        
        def missing(idx, nums):
            return nums[idx] - (nums[0] + idx)
        
        N = len(nums)
        # Special case: k > missing(n-1, nums)
        if missing(N - 1, nums) < k:
            return nums[N-1] + (k-missing(N-1, nums))
        
        low = 0
        high = N - 1
        while low != high:
            mid = (low+high) // 2 
            if missing(mid, nums) < k:
                low = mid + 1
            else:
                high = mid
        
        return nums[low-1] + (k-missing(low-1, nums))
        