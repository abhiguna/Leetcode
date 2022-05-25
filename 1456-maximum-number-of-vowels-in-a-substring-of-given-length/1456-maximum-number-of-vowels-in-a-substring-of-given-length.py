class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxVowels(self, s: str, k: int) -> int:
        N = len(s)
        # Initialization
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        count = 0
        
        for i in range(k):
            if s[i] in vowels:
                count += 1
        
        # General case
        max_count = count
        
        for i in range(k, N):
            if s[i] in vowels:
                count += 1
            
            if s[i-k] in vowels:
                count -= 1
            
            # Update max_count
            max_count = max(max_count, count)
        
        return max_count