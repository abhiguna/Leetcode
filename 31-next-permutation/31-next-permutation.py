class Solution:
    # Time = O(N)
    # Space = O(1)
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        
        # Find pivot 
        pivot = 0
        for i in range(N-1, 0, -1):
            if nums[i-1] < nums[i]:
                pivot = i
                break
        
        # Edge case: already at the last element of the permutations
        if pivot == 0:
            nums.reverse()
            return
        
        # Then find the swap -> first number > than pivot
        swap_idx = N-1
        while nums[pivot-1] >= nums[swap_idx]:
            swap_idx -= 1
        
        # Swap
        (nums[pivot-1], nums[swap_idx]) = (nums[swap_idx], nums[pivot-1])
        
        # Reverse from pivot to end
        nums[pivot:] = nums[N-1:pivot-1:-1]
        return