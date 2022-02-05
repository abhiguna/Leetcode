# Date: 2/5/22
# 30m 5
from collections import defaultdict
class Solution:
    # Time = O(n)
    # Space = O(1) ~ size of hashmap is limited to 60
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if len(time) < 2:
            return 0
        diff_dict = defaultdict(list)
        total = 0
        for length in time:
            mod = length % 60
            if mod in diff_dict:
                total += 1 * len(diff_dict[mod])
            if mod == 0:
                diff_dict[0].append(length)
            else:
                diff = 60 - (length % 60)
                diff_dict[diff].append(length)
        return total
                