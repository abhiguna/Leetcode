class Solution:
    # Time = O(N) worst case, O(logN) best case if no duplicates in input array
    # Space = O(1)
    def search(self, nums: List[int], target: int) -> bool:
        N = len(nums)
        
        # Edge case: N == 1
        if N == 1:
            return (nums[0] == target)
        if nums[-1] == target:
            return True
        
        start = 0
        # We find the first idx where nums[start] != nums[-1]
        for i in range(start, N):
            if nums[i] != nums[-1]:
                start = i
                break
        # Edge case: if all elements are equal
        if i == N:
            return (nums[-1] == target)
        
        end = N - 1
        target_zone = "rotated" if target > nums[-1] else "non-rotated"
        
        while start <= end:
            mid = start + (end-start) // 2
            if nums[mid] == target:
                return True
            # We move mid towards the target zone
            if target_zone == "rotated" and nums[mid] <= nums[-1]:
                end = mid - 1
            elif target_zone == "non-rotated" and nums[mid] > nums[-1]:
                start = mid + 1
            # mid is in the target zone -> regular binsearch
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
        
        # Target not found
        return False
                
            
            
            