class Solution:
    # Time = O(N)
    # Space = O(N)
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = deque()
        N = len(heights)
        
        for i in range(N):
            # Pop out all the elements that have a height <= current height
            while stack and stack[-1][0] <= heights[i]:
                stack.pop()
            stack.append((heights[i], i))
        
        res = []
        for (height, idx) in stack:
            res.append(idx)
        
        return res
            