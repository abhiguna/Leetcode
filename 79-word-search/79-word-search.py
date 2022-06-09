class Solution:
    # Time = O(4^(M+N))
    # Space = O(M+N)
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N = len(board), len(board[0])
        visited = set()
        
        def dfs(idx, row, col):
            # Base case
            if idx == len(word):
                return True
            # Backtracking case
            if row < 0 or row >= M or col < 0 or col >= N or word[idx] != board[row][col] or (row, col) in visited:
                return False
            
            # General case
            visited.add((row, col))
            res = dfs(idx+1, row+1, col) or dfs(idx+1, row-1, col) or dfs(idx+1, row, col-1) or dfs(idx+1, row, col+1)
            visited.remove((row, col))
            return res
        
        # Outer loop
        for i in range(M):
            for j in range(N):
                found = dfs(0, i, j)
                if found: return True
        return False
    