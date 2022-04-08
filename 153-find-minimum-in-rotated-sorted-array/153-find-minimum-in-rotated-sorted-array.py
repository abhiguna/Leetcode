class Solution:
    # Time = O(logN)
    # Space = O(1)
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[0]
        
        N = len(nums)
        start = 0
        end = N - 1
        
        while start <= end:
            if nums[start] <= nums[end]:
                min_val = min(min_val, nums[start])
                break
            
            mid = start + (end-start) // 2
            min_val = min(min_val, nums[mid])
            
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        
        return min_val