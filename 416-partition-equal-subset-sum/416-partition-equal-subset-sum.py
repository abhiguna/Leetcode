class Solution:
    # Time = O(N*S)
    # Space = O(N*S)
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        S = sum(nums)
        
        # Edge case: total sum is odd
        if S % 2 == 1:
            return False
        
        table = [[False for j in range((S//2)+1)] for i in range(N+1)]
        table[0][0] = True
        
        # Base cases
        # Fill first column
        for i in range(1, N+1):
            table[i][0] = True
        
        # Fill first row
        for j in range(1, (S//2) + 1):
            table[0][j] = False
        
        # Fill remaining cells
        for i in range(1, N+1):
            for amount in range(1, (S//2) + 1):
                # Exclude case
                table[i][amount] = table[i-1][amount]
                
                # Include case
                if nums[i-1] <= amount:
                    table[i][amount] = table[i][amount] or table[i-1][amount-nums[i-1]]
        
        return table[N][S//2]
                
        