class Solution:
    # Time = O(N)
    # Space = O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        # Cycle sort
        for i in range(N):
            while nums[i] != i+1:
                dest = nums[i] - 1
                # Sanity check: not a duplicate at dest idx
                if nums[dest] != nums[i]:
                    # Swap
                    nums[i], nums[dest] = nums[dest], nums[i]
                else:
                    break
        
        # Find all duplicates
        dups = []
        for i in range(N):
            if nums[i] != i+1:
                dups.append(nums[i])
        
        return dups