class Solution:
    # Time = O(N)
    # Space = O(1)
    def calculate(self, s: str) -> int:
        N = len(s)
        
        # Keep track of the prev and curr result
        prev, curr = 0, 0
        res = 0
        
        # By default the operation is addition
        op = "+"
        
        i = 0
        while i < N:
            # 3 cases to consider
            
            # Digit
            if s[i].isdigit():
                # Get all the digits of a number
                while i < N and s[i].isdigit():
                    curr = (curr * 10) + int(s[i])
                    i += 1
                
                # We would be one spot to the right of the rightmost digit
                i -= 1
                
                # curr contains the curr digit, prev points to the previous result
                if op == "+":
                    res += curr
                    prev = curr
                elif op == "-":
                    res -= curr
                    # Set the curr to its negation
                    prev = -curr
                    
                # Undo the previous operation before performing a '*' or a '/'
                elif op == "*":
                    res -= prev
                    res += (prev * curr)
                    prev = (prev * curr)
                    
                else: # "/"
                    res -= prev
                    res += int(prev / curr)
                    prev = int(prev / curr)
                    
                    
                curr = 0
                    
            
            # Operator
            elif s[i] != " ":
                op = s[i]
                
            # Space
            i += 1
        
        return res