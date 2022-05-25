class Solution:
    # Time = O(N)
    # Space = O(1)
    def findAnagrams(self, s: str, p: str) -> List[int]:
        M, N, k = len(s), len(p), len(p)
        # Edge case: if N > M return 0
        if N > M:
            return []
        hmap_p = Counter(p)
        hmap_s = defaultdict(int)
        
        res = []
        # Add the chars of the first window to the hashmap
        for i in range(k):
            hmap_s[s[i]] += 1
            
            if hmap_s == hmap_p:
                res.append(i-k+1) # i-k+1 is the start idx
        
        for i in range(k, M):
            hmap_s[s[i-k]] -= 1
            
            if hmap_s[s[i-k]] == 0:
                del hmap_s[s[i-k]]
                
            hmap_s[s[i]] += 1
            
            if hmap_s == hmap_p:
                res.append(i-k+1)
        
        return res
        
            