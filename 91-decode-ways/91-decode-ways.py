class Solution:
    # Approach: DP
    
    # Time = O(N)
    # Space = O(N) -> could be brought down to O(1)
    def numDecodings(self, s: str) -> int:
        N = len(s)
        table = [0 for i in range(N+1)]
        table[0] = 1 # One way to decode an empty string
        table[1] = 1 if s[0] != "0" else 0
        
        for i in range(2, N+1):
            # Check if the curr digit is valid
            if s[i-1] in "123456789":
                table[i] += table[i-1]
                
            # Check if the last two digits are valid
            if s[i-2] == "1" or (s[i-2] == "2" and s[i-1] in "0123456"):
                table[i] += table[i-2]
        
        return table[N]