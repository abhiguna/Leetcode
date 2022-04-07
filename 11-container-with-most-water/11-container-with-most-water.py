class Solution:
    
    # Time = O(N)
    # Space = O(1)
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        curr_area = 0
        max_area = 0
        
        left = 0
        right = N - 1
        
        while left <= right:
            curr_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, curr_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area