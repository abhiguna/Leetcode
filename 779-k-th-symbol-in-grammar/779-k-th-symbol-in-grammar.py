class Solution:
    # Time = O(N)
    # Space = O(N)
    def kthGrammar(self, n: int, k: int) -> int:
        # Base case
        if n == 1 and k == 1:
            return 0
        
        mid = (2**(n-1)) // 2
        if k <= mid:
            return self.kthGrammar(n-1, k)
        else:
            ret_val = self.kthGrammar(n-1, k-mid)
            if ret_val == 0:
                return 1
            else:
                return 0