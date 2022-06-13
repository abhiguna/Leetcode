class Solution:
    # Time = O(n^2)
    # Space = O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        word_set = set(wordDict)
        table = [False] * (n)
        
        for j in range(n):
            for i in range(j, -1, -1):
                if (s[i:j+1] in word_set) and ((i > 0 and table[i-1]) or (i == 0)):
                    table[j] = True
        
        return table[n-1]