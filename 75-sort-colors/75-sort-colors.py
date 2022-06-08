class Solution:
    # Time = O(N)
    # Space = O(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        red = 0
        white = 0
        blue = N - 1
        
        while white <= blue:
            if nums[white] == 1:
                white += 1
            elif nums[white] == 0:
                # Swap with red
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            else:
                # Swap with blue
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        
        return