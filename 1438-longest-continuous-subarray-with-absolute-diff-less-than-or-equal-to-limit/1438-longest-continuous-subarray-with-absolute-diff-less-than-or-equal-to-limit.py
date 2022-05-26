class Solution:
    # Time = O(N)
    # Space = O(N)
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        # We need to keep track of both the sliding window max and sliding window min in order to compute the range
        max_deque = deque() # Stores the values in an increasing range
        min_deque = deque() # Stores the values in a decreasing range
        max_len = 0
        left = 0
        
        for i in range(N):
            # Update the maximum value
            while max_deque and max_deque[-1] < nums[i]:
                max_deque.pop()
            
            max_deque.append(nums[i])
            
            # Update the minimum value
            while min_deque and min_deque[-1] > nums[i]:
                min_deque.pop()
            
            min_deque.append(nums[i])
            
            # Move sliding window
            while left <= i and (max_deque[0] - min_deque[0] > limit):
                # Remove respective entries from max_deque and min_deque
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                left += 1
            
            # Update max_len
            max_len = max(max_len, i-left+1)
        return max_len
    
        