class Solution:
    # Time = O(N)
    # Space = O(1)
    def sortColors(self, nums: List[int]) -> None:
        N = len(nums)
        red = 0
        blue = N - 1
        read = 0
        
        while read <= blue:
            if nums[read] == 0:
                # Swap with red
                nums[red], nums[read] = nums[read], nums[red]
                red += 1
                read += 1
            elif nums[read] == 1:
                read += 1
            else:
                # Swap with blue
                nums[blue], nums[read] = nums[read], nums[blue]
                blue -= 1
        
        return nums
        