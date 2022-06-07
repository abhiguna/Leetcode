class Solution:
    # Time = O(M + N)
    # Space = O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        M, N = len(s), len(t)
        
        # Edge case
        if M != N:
            return False
        
        hmap = Counter(t)
        
        for c in s:
            if c not in hmap:
                return False
            
            hmap[c] -= 1
            if hmap[c] == 0:
                del hmap[c]
        
        return (len(hmap) == 0)