class Solution:
    # Time = O(logN)
    # Space = O(1)
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        start = 0
        end = N - 1
        while start <= end:
            mid = start + (end - start) // 2
            # Target found
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        
        return -1