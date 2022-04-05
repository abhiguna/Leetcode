class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        
        dp = [False for i in range(N + 1)]
        
        # Base case
        dp[N] = True
        
        for i in range(N - 1, -1, -1):
            for word in wordDict:
                if (i + len(word)) <= N and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                
                # Word match found at idx i -> stop checking more words in wordDict
                if dp[i]:
                    break
        
        return dp[0]
                    