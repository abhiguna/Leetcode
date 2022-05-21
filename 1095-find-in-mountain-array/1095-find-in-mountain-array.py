# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        N = mountain_arr.length()
        peak_idx = -1
        
        # Find the peak
        start = 0
        end = N - 1
        while start <= end:
            mid = start + (end-start) // 2
            mid_val = mountain_arr.get(mid)
            succ_val = mountain_arr.get(mid+1) if mid != N-1 else -1
            pred_val = mountain_arr.get(mid-1) if mid != 0 else -1
            # Check for peak
            if mid != 0 and mid != N-1 and mid_val > pred_val and mid_val > succ_val:
                peak_idx = mid
                # Check if peak == target
                if mid_val == target:
                    return peak_idx
                break
            elif mid == 0 or mid_val < succ_val:
                start = mid + 1
            else:
                end = mid - 1
        
        # Binsearch from [0, peak-1]
        start = 0
        end = peak_idx - 1
        while start <= end:
            mid = start + (end-start) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                start = mid + 1
            else:
                end = mid - 1
        
        # Binsearch from [peak+1, N-1]
        start = peak_idx + 1
        end = N - 1
        while start <= end:
            mid = start + (end-start) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            elif mid_val < target:
                end = mid - 1
            else:
                start = mid + 1
        
        # Target not found
        return -1