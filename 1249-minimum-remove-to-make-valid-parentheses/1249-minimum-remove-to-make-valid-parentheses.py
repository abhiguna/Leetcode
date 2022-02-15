class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        valid = []
        N = len(s)
        j = 0
        for i in range(N):
            if s[i].isalpha():
                valid.append(s[i])
                j += 1
            elif s[i] == '(':
                stack.append(('(', j))
                valid.append('(')
                j += 1
            else:
                if not stack:
                    continue
                stack.pop()
                valid.append(')')
                j += 1
        while stack:
            paran = stack.pop()
            valid[paran[1]] = ''  
        return "".join(valid)
                
        