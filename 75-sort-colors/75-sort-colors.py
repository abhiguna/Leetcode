class Solution:
    # Time = O(N)
    # Space = O(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, read, right = 0, 0, len(nums) - 1
        
        while read <= right:
            if nums[read] == 1:
                read += 1
            elif nums[read] == 0:
                (nums[left], nums[read]) = (nums[read], nums[left])
                left += 1
                read += 1
            else:
                (nums[right], nums[read]) = (nums[read], nums[right])
                right -= 1
        
        return nums