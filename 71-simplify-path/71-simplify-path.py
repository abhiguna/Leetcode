# Date: 2/16/22
# 20m 3
class Solution:
    # Pattern: Stack
    # Time = O(n)
    # Space = O(n)
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""
        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur and cur != ".":
                    stack.append(cur)
                cur = ""
            else:
                cur += c
        return "/" + "/".join(stack)