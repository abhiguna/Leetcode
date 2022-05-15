class Solution:
    # Approach: DP

    # Time = O(N^3)
    # Space = O(N^2)
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        N = len(nums)
        table = [[0 for col in range(N)] for row in range(N)]
        # table[row][col] = the max value for bursting baloons in the range[i, j]
        # table[row][col] = max(table[row][k] + table[k][col] + nums[row]*nums[k]*nums[col])

        # Base case: 
        for row in range(N-1):
            table[row][row+1] = 0

        # Recursive case: Fill the table from the bottom row to the top row from left to right
        for row in range(N-2, -1, -1):
            for col in range(row+2, N):
                for k in range(row+1, col):
                    table[row][col] = max(table[row][col], table[row][k] + table[k][col] + (nums[row]*nums[k]*nums[col]))

        # Final answer will be stored in M[0][N-1] when the entire set of matrices are considered
        return table[0][N-1]