# Not Optimal

# Date: 2/6/22
# 30m 5
class Solution:
    # Pattern = ad-hoc
    # Time = O(n)
    # Space = O(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_red = 0
        num_white = 0
        num_blue = 0
        for color in nums:
            if color == 0:
                num_red += 1
            elif color == 1:
                num_white += 1
            else:
                num_blue += 1
        N = len(nums)
        idx = 0
        while idx<N and num_red>0:
            nums[idx] = 0
            idx += 1
            num_red -= 1
        while idx<N and num_white>0:
            nums[idx] = 1
            idx += 1
            num_white -= 1
        while idx<N and num_blue>0:
            nums[idx] = 2
            idx += 1
            num_blue -= 1    
        return
        