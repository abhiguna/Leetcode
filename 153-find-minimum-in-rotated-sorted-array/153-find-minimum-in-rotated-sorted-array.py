class Solution:
    
    # Time = O(logN)
    # Space = O(1)
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        
        start = 0
        end = N - 1
        res = math.inf
        
        while start <= end:
            # No net rotations
            if nums[start] <= nums[end]:
                res = min(res, nums[start])
                break
            
            mid = start + (end - start) // 2
            res = min(res, nums[mid])
            # Rotations and mid in left sorted part -> search right
            if nums[mid] >= nums[start]:
                start = mid + 1
            # Rotations and mid in right sorted part -> search left
            else:
                end = mid - 1
        
        return res
            