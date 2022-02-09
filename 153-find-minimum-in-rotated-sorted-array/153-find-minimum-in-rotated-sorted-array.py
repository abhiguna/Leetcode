# sorted + unique --> bin search
# [3, 4, 5, 1, 2, 2.5]
# mid > mid_right --> low = mid + 1
# mid > mid_left --> high = mid - 1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        low = 0
        high = len(nums) - 1
        mid_left = -math.inf
        mid_right = -math.inf
        while low <= high:
            mid = (low+high) // 2
            if mid > 0:
                mid_left = nums[mid - 1]
            if mid + 1 < len(nums):
                mid_right = nums[mid + 1]
            
            if nums[high] < nums[low]: # Rotated
                if nums[mid] < nums[low]:
                    high = mid
                else:
                    low = mid + 1
            else: # Not rotated
                return nums[low]
        return nums[low]
    