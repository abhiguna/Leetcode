class Solution:
    # Time = Exponential
    # Space = Exponential
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        solution = [None] * n
        final_solution = []
        
        # Dp arrays 
        dp_col = [False] * n
        dp_slash = [False] * (2*n - 1)
        dp_backslash = [False] * (2*n - 1)
        
        def can_place(row, col):
            return not (dp_col[col] or dp_slash[row + col] or dp_backslash[(row-col) + n - 1])
            
        def dfs(curr_row, queens_left, slate):
            # Base case
            if curr_row == n:
                if queens_left == 0:
                    res.append(list(slate))
                return
            
            for curr_col in range(n):
                if can_place(curr_row, curr_col):
                    slate[curr_row] = curr_col
                    dp_col[curr_col] = True
                    dp_slash[curr_row + curr_col] = True
                    dp_backslash[(curr_row-curr_col) + (n-1)] = True
                    
                    dfs(curr_row + 1, queens_left - 1, slate)
                    
                    dp_col[curr_col] = False
                    dp_slash[curr_row + curr_col] = False
                    dp_backslash[(curr_row-curr_col) + (n-1)] = False
            
            return
        
        def generate_board():
            for sol in res:
                board = [["." for j in range(n)] for i in range(n)]
                for row, col in enumerate(sol):
                    board[row][col] = "Q"
                final_solution.append(["".join(row) for row in board])
        
        dfs(0, n, solution)
        generate_board()
        return final_solution
                    