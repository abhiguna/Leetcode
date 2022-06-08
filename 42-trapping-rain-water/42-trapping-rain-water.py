class Solution:
    # Time = O(N)
    # Space = O(1)
    def trap(self, height: List[int]) -> int:
        N = len(height)
        
        # Edge case: N <= 2
        if N <= 2:
            return 0
        
        trapped_vol = 0
        prev_level = 0
        i = 0
        j = N - 1
        
        while i < j - 1:
            curr_level = min(height[i], height[j])
            
            # Add volume if possible
            if curr_level > prev_level:
                height_diff = curr_level - prev_level
                trapped_vol += (height_diff) * (j-i-1)
                prev_level = curr_level
            
            # Subtract volume by the height of the wall
            if height[i] <= height[j]:
                i += 1
                trapped_vol -= min(prev_level, height[i])
            else:
                j -= 1
                trapped_vol -= min(prev_level, height[j])
                
        
        return trapped_vol