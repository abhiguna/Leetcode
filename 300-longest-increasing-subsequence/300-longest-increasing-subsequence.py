class Solution:
    # Time = O(n^2)
    # Space = O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        def getMax(dp, nums, n):
            max_len = 0
            target = nums[n]
            for i in range(n):
                if nums[i] < target:
                    max_len = max(max_len, dp[i])
            return max_len
            
        dp = [1 for _ in nums]
        longest = 1
        for i in range(len(nums)):
            prev_long = getMax(dp, nums, i)
            dp[i] = max(dp[i], prev_long + 1)
            longest = max(longest, prev_long + 1)
        return longest