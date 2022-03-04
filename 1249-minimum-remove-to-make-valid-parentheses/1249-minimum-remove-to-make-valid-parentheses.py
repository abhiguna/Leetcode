from collections import deque

class Solution:
    # stack -> store (open, idx)
    # str_to_list -> invalid idx = ""
    # paran_mapping
    # cases:
    #1. close but no open before -> mark idx 
    # 2. stack not empty --> mark all invalid idx
    # 3. not matching opening/closing --> mark invalid closing
    def minRemoveToMakeValid(self, s: str) -> str:
        paran_mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        stack = deque()
        s = list(s)
        for idx, char in enumerate(s):
            if char in paran_mapping.values():
                # open paran
                stack.append((char, idx))
                
            elif char in paran_mapping.keys():
                # close paran
                if not stack:
                    s[idx] = ""
                    continue
                    
                top_char, top_idx = stack.pop()
                if top_char != paran_mapping[char]:
                    s[idx] = ""
                    stack.append((top_char, top_idx))
                    
        while stack:
            remove_char, remove_idx = stack.pop()
            s[remove_idx] = ""
        
        return "".join(s)
                    
                
                
                
                
        
        