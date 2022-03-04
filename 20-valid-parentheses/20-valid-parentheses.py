from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        paran_matcher = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = deque()
        for p in s:
            if p not in paran_matcher:
                # opening parantheses
                stack.append(p)
            else:
                # closing parantheses
                if not stack:
                    return False
                top = stack.pop()
                if top != paran_matcher[p]:
                    return False
        return len(stack) == 0