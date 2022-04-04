class Solution:
    
    # Time = O(N)
    # Space = O(1)
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        
        # Cyclic sort
        i = 0
        while i < N:
            swap_idx = nums[i]
            
            if nums[i] < N and nums[i] != nums[swap_idx]:
                # Swap values
                nums[i], nums[swap_idx] = nums[swap_idx], nums[i]
            else:
                i += 1
        
        # Iterate to find missing number
        for i in range(N):
            if nums[i] != i:
                return i
        
        return N
        