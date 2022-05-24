class Solution:
    # Time = O(N)
    # Space = O(1)
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        # We use a D&C approach. if i is odd and nums[i-1] > nums[i] or 
        #. if i is even and nums[i-1] < nums[i], we swap
        for i in range(1, N):
            if (i % 2 == 1 and nums[i-1] >= nums[i]) or \
                (i % 2 == 0 and nums[i-1] <= nums[i]):
                # Swap nums[i-1] and nums[i]
                nums[i-1], nums[i] = nums[i], nums[i-1]
        
        return nums