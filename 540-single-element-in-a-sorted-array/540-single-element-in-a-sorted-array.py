class Solution:
    # Time = O(logN)
    # Space = O(1)
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # Edge cases
        # len(nums) == 1
        if len(nums) == 1:
            return nums[0]
        # Check beginning
        if nums[0] != nums[1]:
            return nums[0]
        # Check end
        if nums[-1] != nums[-2]:
            return nums[-1]
        
        # General case
        # Boundary:  even-odd | unpaired | odd-even
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            # In the left boundary
            if (mid % 2 == 0 and nums[mid+1] == nums[mid]) or \
                (mid % 2 != 0 and nums[mid-1] == nums[mid]):
                start = mid + 1
            # In the right boundary
            else:
                end = mid - 1
        
        # This point will never be reached since the unpaired element will always be returned by the 
        #.   logic above
        return -1