class Solution:
    # Time = O(N*M*4^L), L: len(word)
    # Space = O(L)
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        visited = set()
        
        def dfs(row, col, idx):
            # Base case
            if idx == len(word):
                return True
            if row < 0 or col < 0 or row >= M or col >= N or board[row][col] != word[idx] or \
                (row, col) in visited:
                return False
            
            visited.add((row, col))
            res = dfs(row+1, col, idx+1) or \
                    dfs(row-1, col, idx+1) or \
                    dfs(row, col+1, idx+1) or \
                    dfs(row, col-1, idx+1)
            visited.remove((row, col))
            return res
                
        for r in range(M):
            for c in range(N):
                word_found = dfs(r, c, 0)
                if word_found: return True
        
        return False
        
        
        
            