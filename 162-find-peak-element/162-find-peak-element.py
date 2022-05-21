class Solution:
    # Time = O(logN)
    # Space = O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        # Edge cases
        N = len(nums)
        if N == 1:
            return 0
        # Check array of size 2
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return N-1
        
        
        start = 0
        end = N - 1
        while start <= end:
            mid = start + (end - start) // 2
            # mid is a peak element
            if mid != 0 and mid != N-1 and nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
        
            # mid is a valley element
            elif mid != 0 and mid != N-1 and nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
                # Peak could be in left or right side, we arbitrarily choose the right side
                start = mid + 1
            
            # mid is in ascending zone
            elif mid == 0 or nums[mid] < nums[mid+1]:
                start = mid + 1
        
            # mid is in descending zone
            else:
                end = mid - 1
        
        # No peak found -> this will never be hit
        return -1