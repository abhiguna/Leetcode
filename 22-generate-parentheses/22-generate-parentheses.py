class Solution:
    # Time = O(Catalan Number)
    # Space = O(N)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def helper(num_open, num_close, slate):
            # Backtracking case
            if num_close > num_open:
                return
            # Base case
            elif num_open + num_close == 2*n:
                res.append("".join(slate[:]))
                return
            else:
                # Add an open paran if possible
                if num_open < n:
                    slate.append('(')
                    helper(num_open+1, num_close, slate)
                    slate.pop()
                
                # Add an close paran if possible
                if num_close < n:
                    slate.append(')')
                    helper(num_open, num_close+1, slate)
                    slate.pop()
            return
                
        # Root Manager
        helper(0, 0, [])
        return res
        