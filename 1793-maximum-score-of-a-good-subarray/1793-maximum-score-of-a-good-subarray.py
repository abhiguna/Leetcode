class Solution:
    # Time = O(N)
    # Space = O(N)
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # Compute the left and right spans
        stack = deque()
        left_span = [0] * N
        
        for i in range(N):
            while stack and stack[-1][0] >= nums[i]:
                stack.pop()
            
            if stack:
                left_span[i] = i - stack[-1][1]
            else:
                left_span[i] = i + 1
            
            stack.append((nums[i], i))
        
        stack = deque()
        right_span = [0] * N
        
        for i in range(N-1, -1, -1):
            while stack and stack[-1][0] >= nums[i]:
                stack.pop()
            
            if stack:
                right_span[i] = stack[-1][1] - i
            else:
                right_span[i] = N - i
            
            stack.append((nums[i], i))
        
        max_area = 0
        for i in range(N):
            curr_area = nums[i] * (left_span[i] + right_span[i] - 1)
            if i-left_span[i] + 1 <= k <= i+right_span[i]-1:
                max_area = max(max_area, curr_area)
        
        return max_area
                
            