class Solution:
    # Time = O(N^2)
    # Space = O(N)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        table = [False] * (N+1)
        table[0] = True
        
        for i in range(1, N+1):
            for j in range(0, i+1):
                can_break = table[j] and (s[j:i] in wordDict)
                table[i] = table[i] or can_break
        
        return table[N]
        