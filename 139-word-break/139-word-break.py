class Solution:
    
    # Time = O(N * M)
    # Space = O(N)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        M = len(wordDict)
        
        dp = [False for i in range(N + 1)]
        # Base
        dp[N] = True
        
        for i in range(N-1, -1, -1):
            for word in wordDict:
                # Check matches
                if (i + len(word)) <= N and s[i:i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                
                # Check if more words need to be compared
                if dp[i]:
                    break
        
        return dp[0]