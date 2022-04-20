class Solution:
    def helper(self, n, idx, num_opening, num_closing, partial_solution, res):
            # Base case
            if idx == 2*n:
                res.append("".join(partial_solution[:]))
                return
            
            # Recursive case
            # 1. Opening paran
            if num_opening < n:
                partial_solution.append("(")
                self.helper(n, idx + 1, num_opening + 1, num_closing, partial_solution, res)
                partial_solution.pop()
            
            # 2. Closing paran
            if num_closing < num_opening:
                partial_solution.append(")")
                self.helper(n, idx + 1, num_opening, num_closing + 1, partial_solution, res)
                partial_solution.pop()
            
            return
    
    # Time = O(N*2^N)
    # Space = O(N)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(n, 0, 0, 0, [], res)
        return res
        
        
        