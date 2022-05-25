class Solution:
    # Time = O(N)
    # Space = O(1) => both hmaps contains at most 26 unique keys 
    def checkInclusion(self, s1: str, s2: str) -> bool:
        M, N, k = len(s1), len(s2), len(s1)
        # Edge case: if len(s1) > len(s2)
        if len(s1) > len(s2):
            return False
        
        # Initialize a hmap for s1 and s2
        hmap_s1 = Counter(s1)
        hmap_s2 = defaultdict(int)
        for i in range(k):
            hmap_s2[s2[i]] += 1
            # Check if hmap for s2 is equal to hmap for s1
            if hmap_s2 == hmap_s1:
                return True
        
        # Update the hmap by traversing the remaining parts of s2
        for i in range(k, N):
            hmap_s2[s2[i-k]] -= 1
            if hmap_s2[s2[i-k]] == 0:
                del hmap_s2[s2[i-k]]
            
            hmap_s2[s2[i]] += 1
            # Check if s1 found as a permutation in s2
            if hmap_s2 == hmap_s1:
                return True
        
        # No permutation of s1 found in s2
        return False