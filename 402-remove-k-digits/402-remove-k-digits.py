from collections import deque

class Solution:
    # stack
    # remove_mode
    
    def removeKdigits(self, num: str, k: int) -> str:
        stack = deque()
        
        if k >= len(num):
            return "0"
        
        for n in num:
            while stack and k > 0 and int(n) < int(stack[-1]):
                stack.pop()
                k -= 1
    
            stack.append(n)
        
        while k > 0:
            stack.pop()
            k -= 1
        
        return str(int("".join(stack)))
        