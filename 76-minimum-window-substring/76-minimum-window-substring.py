from collections import *

class Solution:
    # Time = O(N)
    # Space = O(1)
    def minWindow(self, s: str, t: str) -> str:
        M, N = len(s), len(t)
        hmap_t = Counter(t)
        hmap_s = defaultdict(int)
        
        left = 0
        min_len = math.inf
        min_start, min_end = -1, -1
        
        for i in range(M):
            hmap_s[s[i]] += 1
            while left <= i and all(hmap_s[c] >= hmap_t[c] for c in hmap_t):
                if (i-left+1) < min_len:
                    min_len = i-left+1
                    min_start = left
                    min_end = i
                        
                hmap_s[s[left]] -= 1
                if hmap_s[s[left]] == 0:
                    del hmap_s[s[left]]
                left += 1
                
        return s[min_start:min_end+1] if min_len != math.inf else ""