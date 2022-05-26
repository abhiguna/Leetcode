from collections import *

class Solution:
    # Approach: Sliding window
    
    # Time = O(N)
    # Space = O(1)
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        left = 0
        max_len = 0
        hmap = defaultdict(int) # Stores the distinct type of fruits, which will be at most 3
        
        for i in range(N):
            hmap[fruits[i]] += 1
            
            while len(hmap) > 2:
                hmap[fruits[left]] -= 1
                if hmap[fruits[left]] == 0:
                    del hmap[fruits[left]]
                left += 1
            
            max_len = max(max_len, i-left+1)
        
        return max_len
        
        