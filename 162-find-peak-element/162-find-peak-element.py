# Date: 2/12/22
# 30m 4
class Solution:
    # Pattern: binary search
    # Time = O(logn)
    # Space = O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        low = 0
        high = N - 1
        while low < high:
            mid = (low+high) // 2
            if nums[mid] < nums[mid+1]:
                low = mid + 1
            else:
                high = mid
        return low
        