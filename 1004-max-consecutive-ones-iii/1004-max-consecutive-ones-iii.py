class Solution:
    # Time = O(N)
    # Space = O(1)
    def longestOnes(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left = 0
        window_zeroes = 0
        max_len = 0
        
        for i in range(N):
            if nums[i] == 0:
                window_zeroes += 1
            
            while left <= i and window_zeroes > k:
                if nums[left] == 0:
                    window_zeroes -= 1
                left += 1
            
            max_len = max(max_len, i-left+1)
        
        return max_len