class Solution:
    # Approach 2: Using pointers
    
    # Time = O(N)
    # Space = O(1)
    def findBuildings(self, heights: List[int]) -> List[int]:
        N = len(heights)
        curr_max = heights[N-1]
        res = [N-1]
        for i in range(N-2, -1, -1):
            if heights[i] > curr_max:
                res.append(i)
                curr_max = heights[i]
        # Reverse the result
        res.reverse()
        return res
        