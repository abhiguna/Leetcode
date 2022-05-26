class Solution:
    # Time = O(N)
    # Space = O(1)
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        N = len(s)
        max_len = 0
        left = 0
        hmap = defaultdict(int) # distinct types of letters
        
        for i in range(N):
            hmap[s[i]] += 1
            
            while left <= i and len(hmap) > 2:
                hmap[s[left]] -= 1
                
                if hmap[s[left]] == 0:
                    del hmap[s[left]]
                
                left += 1
                
            # Update max_len
            max_len = max(max_len, i-left+1)
        
        return max_len