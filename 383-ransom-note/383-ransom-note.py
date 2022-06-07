class Solution:
    # Time = O(M+N)
    # Space = O(1)
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        M, N = len(ransomNote), len(magazine)
        
        hmap = Counter(magazine)
        for c in ransomNote:
            if c not in hmap:
                return False
            else:
                hmap[c] -= 1
                if hmap[c] == 0:
                    del hmap[c]
        
        return True