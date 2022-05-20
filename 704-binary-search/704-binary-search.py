class Solution:
    # Time = O(logN)
    # Space = O(1)
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        low = 0
        high = N - 1
        while low <= high:
            mid = low + (high - low) // 2
            # Target found
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1