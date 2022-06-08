class Solution:
    # Time = O(1)
    # Space = O(1)
    def myAtoi(self, s: str) -> int:
        N = len(s)
        # Edge case
        if N == 0:
            return 0
        
        def check_overflow(ans, d, limit):
            limit = (limit - d) / 10
            if ans >= limit:
                return True
            return False
            
        
        is_positive = True
        
        # Process until digit arrives
        idx = 0
        
        # Ignore leading whitespace
        while idx < N and s[idx] == " ":
            idx += 1
        
        # Process sign char if exists
        if idx < N and (s[idx] == "+" or s[idx] == "-"):
            if s[idx] == "-":
                is_positive = False
            idx += 1
        
        # Edge case: check if non-digit chars present
        while idx < N and not s[idx].isdigit():
            return 0
        
        # Process all the digits
        res = 0
        while idx < N and s[idx].isdigit():
            digit = ord(s[idx]) - ord("0")
            
            # Check overflow
            if is_positive:
                if check_overflow(res, digit, (2**31)-1):
                    return (2**31) - 1
            else:
                if check_overflow(res, digit, (2**31)):
                    return -1*(2**31)
            
            # No overflow possible
            res = (res * 10) + digit
            idx += 1
        
        # Process sign and return
        return res if is_positive else -1*res
        
        
        
        