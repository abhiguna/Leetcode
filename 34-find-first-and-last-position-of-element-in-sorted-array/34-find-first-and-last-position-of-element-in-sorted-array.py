class Solution:
    # Time = O(N)
    # Space = O(1)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        start = 0
        end = N - 1
        
        # Find the leftmost idx
        # < target | >= target
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        # Edge case: target not found
        # Occurs when all values are less than target or start points to the first value greater than target
        if start == N or nums[start] != target:
            return [-1, -1]
        
        leftmost_idx = start
        
        # Find the rightmost idxx
        # <= target | > target
        end = N - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        rightmost_idx = end
        return [leftmost_idx, rightmost_idx]