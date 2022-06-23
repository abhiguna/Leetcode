class Solution:
    # Time = O(n*volume)
    # Space = O(1)
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        n = len(heights)
        
        # Insert one droplet at a time
        for _ in range(volume):
            left, right = k, k
            # Check if a smaller height exists to the left
            for i in range(k-1, -1, -1):
                if heights[i] > heights[left]:
                    break
                elif heights[i] < heights[left]:
                    left = i
            
            if left < k:
                heights[left] += 1
            # Check if a smaller height exists to the right
            else:
                for i in range(k+1, n):
                    if heights[i] > heights[right]:
                        break
                    elif heights[i] < heights[right]:
                        right = i
                
                if right > k:
                    heights[right] += 1
            
            # Increment the height at the current idx
            if left == k and right == k:
                heights[k] += 1
        
        return heights
                