from collections import *

class Solution:
    # Time = O(N)
    # Space = O(N)
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        hmap = defaultdict(int) # Stores the idx of each character in the window
        max_len = 0
        left = 0
        
        for i in range(N):
            hmap[s[i]] += 1
            
            while left <= i and hmap[s[i]] > 1:
                hmap[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, i-left+1)
        
        return max_len