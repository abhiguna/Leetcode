class Solution:
    # Time = O(N)
    # Space = O(1)
    def calculate(self, s: str) -> int:
        # Curr keeps track of the current digit
        curr = 0
        # Stores the result computed so far
        res = 0
        # Default sign is positive
        sign = 1
        
        # Need stack to store the previous result and sign bit
        stack = []
        
        for char in s:
            # Five cases
            # Digit
            if char.isdigit():
                curr = (curr * 10) + int(char)
            # Operator
            elif char in ['+', '-']:
                res += (sign * curr)
                sign = 1 if char == "+" else -1
                # Reset curr to be 0
                curr = 0
            # Opening paran
            elif char == "(":
                # Store current res and sign
                stack.append(res)
                stack.append(sign)
                # Reset res and sign
                res = 0
                sign = 1
            # Closing paran
            elif char == ")":
                res += (sign * curr)
                # Multiply curr result by the sign of prev result
                res *= stack.pop()
                # Add prev result to curr result
                res += stack.pop()
                # Reset curr to be 0
                curr = 0
            # Whitespace => do nothing
        
        return res + (sign * curr)
            
        
        