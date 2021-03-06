class Solution:
    # Time = O(M*N)
    # Space = O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        rem_elements = M*N
        res = []
        
        # (0, 0) => (prev_r, prev_c+1) => (0, -1)
        prev_r, prev_c = 0, -1
        while rem_elements > 0:
            # Move right
            (r, c) = (prev_r, prev_c+1)
            while (0 <= r < M) and (0 <= c < N) and matrix[r][c] != math.inf:
                res.append(matrix[r][c])
                matrix[r][c] = math.inf 
                rem_elements -= 1
                (prev_r, prev_c) = (r, c)
                (r, c) = (r, c+1)
            
            # Move down
            (r, c) = (prev_r+1, prev_c)
            while (0 <= r < M) and (0 <= c < N) and matrix[r][c] != math.inf:
                res.append(matrix[r][c])
                matrix[r][c] = math.inf 
                rem_elements -= 1
                (prev_r, prev_c) = (r, c)
                (r, c) = (r+1, c)
            
            # Move left
            (r, c) = (prev_r, prev_c-1)
            while (0 <= r < M) and (0 <= c < N) and matrix[r][c] != math.inf:
                res.append(matrix[r][c])
                matrix[r][c] = math.inf 
                rem_elements -= 1
                (prev_r, prev_c) = (r, c)
                (r, c) = (r, c-1)
            
            # Move up
            (r, c) = (prev_r-1, prev_c)
            while (0 <= r < M) and (0 <= c < N) and matrix[r][c] != math.inf:
                res.append(matrix[r][c])
                matrix[r][c] = math.inf 
                rem_elements -= 1
                (prev_r, prev_c) = (r, c)
                (r, c) = (r-1, c)
        
        return res
        
        