class Solution:
    # Time = O(M+N), M: len(a), N: len(b)
    # Space = O(1)
    def addBinary(self, a: str, b: str) -> str:
        # Get the input strings in LSB-MSB order by reversing it
        a = a[::-1]
        b = b[::-1]
        carry = 0
        res = []
        
        for i in range(max(len(a), len(b))):
            digit_a = ord(a[i]) - ord("0") if i < len(a) else 0
            digit_b = ord(b[i]) - ord("0") if i < len(b) else 0
            
            # Get the sum digit and update the carry
            total = digit_a + digit_b + carry
            sum_digit = total % 2
            carry = total // 2
            res.append(str(sum_digit))
        
        # Append an extra carry if the carry bit is not 0
        if carry > 0:
            res.append(str(carry))
        
        # Reverse the res to get MSB-LSB order
        res = res[::-1]
        return "".join(res)
        
            
        