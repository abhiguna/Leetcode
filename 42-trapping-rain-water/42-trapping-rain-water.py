class Solution:
    # Time = O(N)
    # Space = O(1)
    def trap(self, height: List[int]) -> int:
        N = len(height)
        trapped_vol = 0
        curr_level = 0
        i = 0
        j = N - 1
        
        while i < j - 1:
            my_level = min(height[i], height[j])
            
            # Increase trapped volume only when there is an increase in height
            if my_level > curr_level:
                trapped_vol += (my_level-curr_level) * (j-i-1)
                curr_level = my_level
            
            if height[i] <= height[j]:
                i += 1
                # Decrement trapped volume
                trapped_vol -= min(curr_level, height[i])
            else:
                j -= 1
                # Decrement trapped volume
                trapped_vol -= min(curr_level, height[j])
        
        return trapped_vol