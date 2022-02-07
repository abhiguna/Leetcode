# Optimal
from collections import defaultdict
# Date: 2/7/22
# 30m 3
class Solution:
    # Pattern: hashmap
    # Time = O(n)
    # Space = O(n)
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        curr_sum = 0
        prefix_sums = {0:1}
        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            result += prefix_sums.get(diff, 0)
            prefix_sums[curr_sum] = 1 + prefix_sums.get(curr_sum, 0)
        return result