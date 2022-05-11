class Solution:
    # Approach: DP

    # Time = O(N)
    # Space = O(N)
    def knightDialer(self, n: int) -> int:
        # f(n, d) = number of distinct n-digit numbers that end with digit d
        
        table = [[0 for j in range(10)] for i in range(n+1)]
        
        # Base case: fill the first row with 1 -> exactly one way to fill a phone num of len 1
        #           with digit d
        for j in range(10):
            table[1][j] = 1
        
        knight_map = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        
        for i in range(2, n+1):
            for d in range(10):
                if d == 5:
                    continue
                for prev_digit in knight_map[d]:
                    table[i][d] += table[i-1][prev_digit]
        
        return sum(table[n]) % (10**9 + 7)