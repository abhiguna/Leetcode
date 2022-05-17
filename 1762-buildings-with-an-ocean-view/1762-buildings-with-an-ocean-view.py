class Solution:
    # Time = O(N)
    # Space = O(N)
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = deque([0])
        N = len(heights)
        for i in range(1, N):
            # Remove all the buildings that gets blocked from ocean view
            while len(stack) > 0 and heights[i] >= heights[stack[-1]]:
                stack.pop()
            stack.append(i)
        return list(stack)
        