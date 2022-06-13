class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        
        def helper(sub):
            if sub in memo:
                return memo[sub]
            
            res = []
            
            for i in range(len(sub)):
                prefix = sub[:i+1]
                if prefix in word_set:
                    # Prefix is the entire substring
                    if prefix == sub:
                        res.append(prefix)
                    else:
                        rem_words = helper(sub[i+1:])
                        for phrase in rem_words:
                            res.append(prefix + " " + phrase)
            
            memo[sub] = res
            return res
        
        return helper(s)