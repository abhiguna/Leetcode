class Solution:
    # Time = O(logN)
    # Space = O(1)
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
    
        # Edge case: N == 1
        if N == 1:
            return 0 if nums[0] == target else -1
        
        # Find the zone of the target (rotated | non-rotated)
        target_zone = "rotated" if target > nums[-1] else "non-rotated"
        start = 0
        end = N - 1
        while start <= end:
            # Check if mid and target_zone are different
            mid = start + (end-start) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[-1] and target_zone == "non-rotated":
                # Move mid towards non-rotated zone
                start = mid + 1
            elif nums[mid] <= nums[-1] and target_zone == "rotated":
                # Move mid towards rotated zone
                end = mid - 1
            else:
                # mid and target_zone are the same -> regular binsearch
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            
        # Target not found
        return -1