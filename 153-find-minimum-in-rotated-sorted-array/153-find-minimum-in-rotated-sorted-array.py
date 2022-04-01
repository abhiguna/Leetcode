class Solution:
    
    # Time = O(logN)
    # Space = O(1)
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        
        start = 0
        end = N - 1
        res = math.inf
        
        while start <= end:
            # No rotations
            if nums[start] <= nums[end]:
                res = min(res, nums[start])
                break
                
            # Rotated Case
            mid = start + (end - start) // 2
            res = min(res, nums[mid])
            
            # Sorted on the left, search right side
            if nums[mid] >= nums[start]:
                start = mid + 1
            
            # Sorted on the right, search the left side
            else:
                end = mid - 1
            
        return res