class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        
        left = 0
        right = N - 1
        res = 0
        
        while left <= right:
            curr_area = min(height[left], height[right]) * (right - left)
            res = max(res, curr_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return res