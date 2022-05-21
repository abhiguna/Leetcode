class Solution:
    # Time = O(logN)
    # Space = O(1)
    def missingElement(self, nums: List[int], k: int) -> int:
        N = len(nums)
        start = 0
        end = N - 1
        # We have two zones: missing_left < k | missing_left >= k
        # Goal: find the last value in the missing_left < k zone
        while start <= end:
            mid = start + (end - start) // 2
            expected_val = nums[0] + mid
            missing_left = nums[mid] - expected_val
            
            # In the left zone
            if missing_left < k:
                start = mid + 1
            # In the right zone
            else:
                end = mid - 1
        
        # The end ptr points to the left zone
        missing_left = nums[end] - (nums[0] + end)
        return nums[end] + (k - missing_left)