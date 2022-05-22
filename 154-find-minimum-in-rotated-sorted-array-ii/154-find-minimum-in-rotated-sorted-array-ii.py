class Solution:
    # Time = O(N) worst case, O(logN) best case if no dups in input
    # Space = O(1)
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        
        # Edge case: N == 1
        if N == 1:
            return nums[0]
        
        # Boundary: rotated (0,...,N-1) | non-rotated (1,...,N)
        start = 0
        end = N - 1
        while start <= end:
            # Find the first position where the start value defers from the end
            for i in range(start, N):
                if nums[i] != nums[-1]:
                    start = i
                    break
            
            # Edge case: all values are the same -> return any value
            if i == N - 1:
                return nums[-1]
            
            mid = start + (end-start) // 2
            # Rotated subarray
            if nums[mid] > nums[-1]:
                start = mid + 1
            # Non-rotated subarray
            else:
                end = mid - 1
        
        return nums[start]
                