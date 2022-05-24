class Solution:
    # Time = O(N)
    # Space = O(1)
    def runningSum(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = []
        prefix_sum = 0
        for i in range(N):
            prefix_sum += nums[i]
            res.append(prefix_sum)
        return res