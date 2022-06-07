from collections import *

class Solution:
    # Time = O(N)
    # Space = O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        
        # Edge case
        if N <= 1:
            return N
        
        hmap = defaultdict(int)
        left = 0
        max_len = 0
        
        for right in range(N):
            hmap[s[right]] += 1
            
            while hmap[s[right]] > 1:
                hmap[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, right-left+1)
        
        return max_len