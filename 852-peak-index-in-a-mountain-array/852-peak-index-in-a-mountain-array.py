class Solution:
    # Time = O(logN)
    # Space = O(1)
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        N = len(arr)
        start = 0
        end = N - 1
        while start <= end:
            mid = start + (end-start) // 2
            # Found the peak
            if mid != 0 and mid != N-1 and arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            # mid in ascending zone
            elif mid == 0 or arr[mid] < arr[mid+1]:
                start = mid + 1
            # mid in descending zone
            else:
                end = mid - 1
        
        return -1