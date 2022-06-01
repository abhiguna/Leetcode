class Solution:
    # Time = O(N*2^N)
    # Space = O(N) -> height of the call stack
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        N = len(s)
        
        def helper(idx, slate):
            # Base case
            if idx == N:
                # We've exhausted all the characters from the original string
                res.append("".join(slate[:]))
                return
            else:
                # Char is a digit
                if s[idx].isdigit():
                    slate.append(s[idx])
                    helper(idx+1, slate)
                    slate.pop()
                # Char is a letter
                else:
                    # Append the lower case version
                    slate.append(s[idx].lower())
                    helper(idx+1, slate)
                    slate.pop()

                    # Append the upper case version
                    slate.append(s[idx].upper())
                    helper(idx+1, slate)
                    slate.pop()
                    return
        
        
        helper(0, [])
        return res