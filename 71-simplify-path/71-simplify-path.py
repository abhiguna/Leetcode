from collections import *

class Solution:
    # Time = O(N), N: tokens in the path
    # Space = O(N)
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        split_path = path.split("/")
        size = 0
        for token in split_path:
            # Check for "//" and "/."
            if len(token) == 0 or token == ".":
                continue
            # If token = "..", move back one directory
            if token == "..":
                if size > 0:
                    stack.pop()
                    size -= 1
            else:
                stack.append(token)
                size += 1
        
        # If in root directory -> return '/'
        if size == 0:
            return "/"
        
        # Combine the elements in the stack to form the final path
        final_path = ""
        for s in stack:
            final_path = final_path + "/" + s
            
        return final_path
        
        