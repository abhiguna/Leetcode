class Solution:
    # Time = O(N)
    # Space = O(k)
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        N = len(s)
        # Edge case: k > N
        if k > N:
            return 0
        
        # Store the char and freq_count in hmap
        hmap = defaultdict(int)
        for i in range(k):
            hmap[s[i]] += 1
        
        if len(hmap) == k:
            count = 1
        else:
            count = 0
        
        # General case: move the sliding window to the right
        for i in range(k, N):
            # Increment count for current character
            hmap[s[i]] += 1
            
            # Decrement count for char outside curr window
            hmap[s[i-k]] -= 1
            if hmap[s[i-k]] == 0:
                del hmap[s[i-k]]
        
            # If length == k => no repeated char
            if len(hmap) == k:
                count += 1
        
        return count
        