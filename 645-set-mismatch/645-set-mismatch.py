class Solution:
    # Time = O(N)
    # Space = O(1)
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        # Cycle sort
        for i in range(N):
            while nums[i] != i + 1:
                dest = nums[i] - 1
                # Safety check
                if nums[dest] != nums[i]:
                    # Swap
                    nums[i], nums[dest] = nums[dest], nums[i]
                else:
                    break
        
        for i in range(N):
            if nums[i] != i+1:
                # We return [dup num, missing num]
                return [nums[i], i+1]
        
        # We won't reach here
        return []