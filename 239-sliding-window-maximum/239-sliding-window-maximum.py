class Solution:
    # Time = O(N)
    # Space = O(k)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        
        # Initialization
        max_deque = deque()
        
        # Insert the first k elements into the heap
        for i in range(k):
            while max_deque and max_deque[-1] < nums[i]:
                max_deque.pop()
            max_deque.append(nums[i])
        
        res = [] # Stores the max in each iteration
        res.append(max_deque[0])
        
        for i in range(k, N):
            # Remove the first element if the start of the prev sliding window is at the front of the deque
            if nums[i-k] == max_deque[0]:
                max_deque.popleft()
            
            while max_deque and max_deque[-1] < nums[i]:
                max_deque.pop()
            max_deque.append(nums[i])
            
            res.append(max_deque[0])
        
        return res