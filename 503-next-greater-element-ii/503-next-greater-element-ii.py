class Solution:
    # Time = O(N)
    # Space = O(N)
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        # Initialization -> populate stack with the array elements
        stack = deque()
        for i in range(N-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            stack.append(nums[i])
        
        res = [-1] * N
        for i in range(N-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            
            # If stack is not empty, found a next greater element
            if stack:
                res[i] = stack[-1]
            
            stack.append(nums[i])
        
        return res