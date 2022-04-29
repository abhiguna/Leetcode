class Solution:
    
    """
        "0" n = 1
        "01" n = 2
        "0110" n = 3
        "01101001" n = 4, k = 5
        
    """
    def kthGrammar(self, n: int, k: int) -> int:
        # Base Case
        if n == 1 and k == 1:
            return 0
        
        mid = (2**(n-1)) // 2
        
        if k <= mid:
            return self.kthGrammar(n-1, k)
        else:
            ret_val = self.kthGrammar(n-1, k-mid)
            if ret_val == 1:
                return 0
            return 1