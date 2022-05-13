class Solution:
    # Approach: DP
    
    # Time = O(N*target)
    # Space = O(target)
    def combinationSum4(self, nums: List[int], target: int) -> int:
        N = len(nums)
        table = [0] * (target+1)
        # table[i] denotes the # of diff. combinations that add up to target
        table[0] = 1
        
        for val in range(1, target+1):
            for num in nums:
                if val - num >= 0:
                    table[val] += table[val-num]
        
        return table[target]