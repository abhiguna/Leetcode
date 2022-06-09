class Solution:
    # Time = O(N)
    # Space = O(1)
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        stack = []
        
        left_span = [0] * N
        # Find the number of elements that have a height greater than or equal to the current element
        for i in range(0, N):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            
            if stack:
                left_span[i] = i - stack[-1][1]
            else:
                left_span[i] = i + 1
            
            stack.append((heights[i], i))
        
        right_span = [0] * N
        stack = []
        for i in range(N-1, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            
            if stack:
                right_span[i] = stack[-1][1] - i
            else:
                right_span[i] = N - i
            
            stack.append((heights[i], i))
        
        max_area = 0
        for i in range(N):
            curr_area = heights[i] * (left_span[i] + right_span[i] - 1)
            max_area = max(max_area, curr_area)
        return max_area
        