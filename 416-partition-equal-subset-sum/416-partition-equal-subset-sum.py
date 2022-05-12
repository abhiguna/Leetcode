class Solution:
    # Approach: DP
    
    # Time = O(N*target)
    # Space = O(N*target) -> could be optimized further to occupy O(target) aux. space
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        # Edge case: if total is odd --> cannot divide evenly into two subsets
        if total % 2 != 0:
            return False
        
        target = total // 2
        table = [[False for j in range(target+1)] for i in range(N+1)]
        # Base cases
        table[0][0] = True # An empty subsets adds up to a target of 0
        
        # Fill first row
        for j in range(1, target+1):
            table[0][j] = False
        
        # Fill first column
        for i in range(1, N+1):
            table[i][0] = False
        
        # Fill remaining cells
        for i in range(1, N+1):
            for val in range(1, target+1):
                # Two choices: exclude or include the current element
                exclude = table[i-1][val]
                include = False
                if val - nums[i-1] >= 0:
                    include = table[i-1][val - nums[i-1]]
                table[i][val] = exclude or include
        
        return table[N][target]
        