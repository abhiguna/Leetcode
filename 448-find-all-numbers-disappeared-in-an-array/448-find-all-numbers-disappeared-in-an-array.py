class Solution:
    # Time = O(N)
    # Space = O(1)
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        # Cycle sort
        for i in range(N):
            while nums[i] != i+1:
                dest = nums[i] - 1
                # Sanity check: check for duplicates
                if nums[i] != nums[dest]:
                    # Swap
                    nums[i], nums[dest] = nums[dest], nums[i]
                else:
                    break
        
        # Find all the missing numbers
        missing_nums = []
        for i in range(N):
            if nums[i] != i+1:
                missing_nums.append(i+1)
        
        return missing_nums