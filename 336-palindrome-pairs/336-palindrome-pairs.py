class Solution:
    # Time = O(k^2*n), n: len(words), k: avg length of a word
    # Space = O((k+n)^2)
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        n = len(words)
        
        def valid_prefixes(s):
            prefixes = []
            for i in range(len(s)):
                # Check if suffix starting at i is a palindrome
                if s[i:] == s[i:][::-1]:
                    prefixes.append(s[:i])
            return prefixes
        
        def valid_suffixes(s):
            suffixes = []
            for i in range(len(s)):
                # Check if prefix ending at i is a palindrome
                if s[:i+1] == s[:i+1][::-1]:
                    suffixes.append(s[i+1:])
            return suffixes
        
        # Build a word map
        word_map = {word: idx for (idx, word) in enumerate(words)}
        res = []
        
        for (idx, word) in enumerate(words):
            # Case 1: word1 and word2 have the same length
            reversed_word = word[::-1]
            # Edge case: if word is a palindrome, check that the reversed word does
            #. not point to the current word
            if (reversed_word in word_map) and (word_map[reversed_word] != idx):
                res.append([idx, word_map[reversed_word]])
            
            # Case 2: len(word1) > len(word2)
            for prefix in valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_map:
                    res.append([idx, word_map[reversed_prefix]])
            
            # Case 3: len(word1) < len(word2)
            for suffix in valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_map:
                    res.append([word_map[reversed_suffix], idx])
        
        return res
        
        