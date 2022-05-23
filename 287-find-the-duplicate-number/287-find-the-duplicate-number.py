class Solution:
    # Time = O(N)
    # Space = O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums)
        
        # Cycle sort: 1, ..., N values in idxs 0,...., N
        for i in range(N):
            while nums[i] != i:
                dest = nums[i]
                # Sanity check
                if nums[i] != nums[dest]:
                    # Swap
                    nums[i], nums[dest] = nums[dest], nums[i]
                else:
                    break
        
        # Find the duplicate
        for i in range(N):
            if nums[i] != i:
                return nums[i]
        
        # Will not be reached since we know there is at least one duplicate
        return -1
        