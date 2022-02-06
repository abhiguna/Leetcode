# Optimal

# Date: 2/6/22
# 30m 3
class Solution:
    # Pattern ad-hoc
    # Time = O(n)
    # Space = O(1)
    def myAtoi(self, s: str) -> int:
        sign = 1
        result = 0
        idx = 0
        N = len(s)
        
        INT_MAX = pow(2, 31) - 1
        INT_MIN = -pow(2, 31)
        
        # Discard all spaces from beginning of the string
        while idx < N and s[idx] == ' ':
            idx += 1
        
        # Update the sign of the number. 
        if idx < N and s[idx] == '-':
            sign = -1
            idx += 1
        elif idx < N and s[idx] == '+':
            sign = 1
            idx += 1
        
        # Traverse the string until a non-digit character is encountered
        while idx < N and s[idx].isdigit():
            digit = int(s[idx])
            
            # Check overflow and underflow conditions
            if ((result > INT_MAX // 10) or (result == INT_MAX // 10 and digit > INT_MAX % 10)):
                # Return number based on overflow or underflow
                return INT_MAX if sign == 1 else INT_MIN
            
            # Append current digit
            result = result * 10 + digit
            idx += 1
        
        # Return final result number after updating its sign
        return sign * result
                
        
        
            