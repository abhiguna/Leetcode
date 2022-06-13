class Solution:
    # Time = O(n), n: len(s)
    # Space = O(n)
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        
        for i in range(n):
            if s[i] != "]":
                stack.append(s[i])
            else:
                # Keep popping all the letters
                sub = deque()
                while stack[-1] != "[":
                    sub.appendleft(stack.pop())
                
                # Pop the open paran
                stack.pop()
                
                # Get the digits
                digit = deque()
                while stack and stack[-1].isdigit():
                    digit.appendleft(stack.pop())
                
                count = int("".join(digit))
                sub = sub * count
                stack.append("".join(sub))
        
        return "".join(stack)
                
        