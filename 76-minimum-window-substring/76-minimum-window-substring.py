from collections import *

class Solution:
    # Time = O(M+N)
    # Space = O(1)
    def minWindow(self, s: str, t: str) -> str:
        M, N = len(s), len(t)
        t_map = Counter(t)
        s_map = defaultdict(int)
        min_len = math.inf
        str_start = -1
        str_end = -1

        left = 0
        for right in range(M):
            s_map[s[right]] += 1
            
            while left <= right and all(s_map[key] >= t_map[key] for key in t_map.keys()):
                if right-left+1 < min_len:
                    min_len = right-left+1
                    str_start = left
                    str_end = right
                    
                s_map[s[left]] -= 1
                left += 1
        
        if str_start == -1:
            return ""
        
        return s[str_start:str_end+1]
        
        
        
        
        