class Solution:
    # Time = O(N)
    # Space = O(1)
    def longestOnes(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left = 0
        max_len = 0
        
        for i in range(N):
            if nums[i] == 0:
                k -= 1
            
            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
            
            max_len = max(max_len, i-left+1)
        
        return max_len