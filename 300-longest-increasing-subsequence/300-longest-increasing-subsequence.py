class Solution:
    # Time = O(n^2)
    # Space = O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        table = [1] * n
        
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                # Check if increasing order
                if nums[j] > nums[i]:
                    table[i] = max(table[i], 1 + table[j])
        
        return max(table)