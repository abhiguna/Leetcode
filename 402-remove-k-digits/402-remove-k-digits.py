from collections import deque

# Optimal
# Time = O(n + k) | Space = O(n)

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
        
        return "".join(stack).lstrip('0') or "0"
        