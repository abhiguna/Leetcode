class Solution:
    # Time = O(N)
    # Space = O(1)
    def romanToInt(self, s: str) -> int:
        N = len(s)
        hmap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        # In the general case, the letters are from largest to smallest except in the edge cases
        
        for i in range(N):
            # Check if the next letter has a larger value than the curr letter
            if i+1 < N and hmap[s[i+1]] > hmap[s[i]]:
                # Subtract the value of the curr char
                total -= hmap[s[i]]
            else:
                total += hmap[s[i]]
        
        return total