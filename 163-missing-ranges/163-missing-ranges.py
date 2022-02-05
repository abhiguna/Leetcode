class Solution:
    # Time = O(n)
    # Space = O(n)
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ranges = []
        if len(nums) == 0:
            diff = upper - lower
            if diff == 0:
                ranges.append(str(lower))
            else:
                ranges.append(str(lower) + "->" + str(upper))
            return ranges
        
        # Special case 1
        if nums[0] > lower:
            num_missing = nums[0] - lower
            if num_missing == 1:
                ranges.append(str(lower))
            else:
                ranges.append(str(lower) + "->" + str(nums[0]-1))
        
        N = len(nums)
        i = 1
        while i < N:
            num_missing = nums[i] - nums[i-1]
            if num_missing == 2:
                ranges.append(str(nums[i-1]+1))
            elif num_missing > 2:
                ranges.append(str(nums[i-1]+1) + "->" + str(nums[i]-1))
            i += 1
        
        # Special case 2
        if nums[-1] < upper:
            num_missing = upper - nums[-1]
            if num_missing == 1:
                ranges.append(str(upper))
            else:
                ranges.append(str(nums[-1]+1) + "->" + str(upper))
        return ranges