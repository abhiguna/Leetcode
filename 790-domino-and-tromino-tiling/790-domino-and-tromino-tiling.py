class Solution:
    # Time = O(N)
    # Space = O(N)
    def numTilings(self, n: int) -> int:
        # Base cases:
        if n <= 2:
            return n
        
        F = [0 for _ in range(n+1)]
        L = [0 for _ in range(n+1)]
        U = [0 for _ in range(n+1)]
        
        F[1], F[2] = 1, 2
        L[1], L[2] = 1, 2
        U[1], U[2] = 1, 2
        
        for idx in range(3, n+1):
            F[idx] = F[idx-1] + F[idx-2] + L[idx-2] + U[idx-2]
            L[idx] = F[idx-1] + U[idx-1]
            U[idx] = F[idx-1] + L[idx-1]
        
        return F[n] % (10**9 + 7)
        
