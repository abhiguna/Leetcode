class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for d in num:
            while k > 0 and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            
            stack.append(d)
        
        # If input given in increasing order -> exclude the last k elements
        if k > 0:
            smallest_sum = stack[:-k]
        else:
            smallest_sum = stack
        
        return ("".join(smallest_sum)).lstrip("0") or "0"