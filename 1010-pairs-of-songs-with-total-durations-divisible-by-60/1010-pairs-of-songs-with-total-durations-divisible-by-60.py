from collections import defaultdict

class Solution:
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
                