class Solution:
    # Time = O(N*4^N)
    # Space = O(N^2)
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case:
        if len(digits) == 0:
            return []
        
        res = []
        N = len(digits)
        
        digit_to_char = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        def dfs(idx, slate):
            # Base case
            if idx == N:
                res.append("".join(slate[:]))
                return
        
            # General case
            for ch in digit_to_char[digits[idx]]:
                slate.append(ch)
                dfs(idx+1, slate)
                slate.pop()
            return
        
        dfs(0, [])
        return res