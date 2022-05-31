class Solution:
    # Time = O(N)
    # Space = O(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        red, white, blue = 0, 0, N-1
        
        while white <= blue:
            if nums[white] == 0:
                # Swap with red
                (nums[red], nums[white]) = (nums[white], nums[red])
                red += 1
                white += 1
            elif nums[white] == 2:
                # Swap with blue
                (nums[blue], nums[white]) = (nums[white], nums[blue])
                blue -= 1
                # DON'T increment the white ptr
            else:
                white += 1
        
        return nums
        
        
        