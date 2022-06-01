class Solution:
    # Time = O(N!)
    # Space = O(N^2)
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for j in range(n)] for i in range(n)]
        res = []
        
        def fill_queens():
            sol = []
            for row in range(n):
                sol.append("".join(board[row]))
            return sol
            
        
        def helper(row, forward_slash, backslash, cols):
            # Base case: placed all the N queens
            if row == n:
                res.append(fill_queens())
                return
            
            # Recursive case
            for col in range(n):
                curr_fslash = row+col
                curr_bslash = row-col
                if (col in cols) or (curr_fslash in forward_slash) or (curr_bslash in backslash):
                    # We cannot place the queen in the current col
                    continue
                
                cols.add(col)
                forward_slash.add(curr_fslash)
                backslash.add(curr_bslash)
                board[row][col] = "Q"
                
                helper(row+1, forward_slash, backslash, cols)
                
                cols.remove(col)
                forward_slash.remove(curr_fslash)
                backslash.remove(curr_bslash)
                board[row][col] = "."
                
            return
    
        helper(0, set(), set(), set())
        return res                