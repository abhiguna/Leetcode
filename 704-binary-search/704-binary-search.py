class Solution:
    # Time = O(logN)
    # Space = O(1)
    def search(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        # Target not found
        if idx == len(nums) or nums[idx] != target:
            return -1
        else:
            return idx