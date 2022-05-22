class Solution:
    # Time = O(logN)
    # Space = O(1)
    def findMin(self, nums: List[int]) -> int:
        # Edge case: N == 1
        N = len(nums)
        if N == 1:
            return nums[0]
        
        # Boundary: rotated subarray 0,1,..,N-1 | non-rotated subarray 1,2,...,N 
        start = 0
        end = N - 1
        while start <= end:
            mid = start + (end - start) // 2
            # If in rotated subarray
            if nums[mid] > nums[-1]:
                start = mid + 1
            # Otherwise, in non-rotated subarray
            else:
                end = mid - 1
        
        return nums[start]
        