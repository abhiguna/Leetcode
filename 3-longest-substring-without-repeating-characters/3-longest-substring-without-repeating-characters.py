class Solution:
    # Time = O(N)
    # Space = O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        left = 0
        max_len = 0
        hmap = defaultdict(int)
        
        for i in range(N):
            if s[i] in hmap and hmap[s[i]] >= left:
                left = hmap[s[i]] + 1
            
            max_len = max(max_len, i-left+1)
            hmap[s[i]] = i
        
        return max_len