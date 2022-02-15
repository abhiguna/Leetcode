# Date: 2/14/22
# 20m 3
class Solution:
    # Pattern: stack
    # Time = O(n + k)
    # Space = O(n)
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        N = len(num)
        i = 0
        while i < N:
            # Remove decreasing order elements
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        # Special case: if num in increasing order
        while k > 0:
            stack.pop()
            k -= 1
        
        min_num = "".join(stack)
        
        # Special Case: remove leading zeroes
        if min_num != "0":
            min_num = min_num.lstrip('0')
        # Special case: empty string
        if min_num == "":
            return "0"
        return min_num
        
        