# Optimal

# Date: 2/7/22
# 30m 5
class Solution:
    # Pattern: BFS
    # Time = O(n * 2^n)
    # Space = O(n) + return array 
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        for num in nums:
            K = len(subsets)
            for i in range(K):
                curr_sub = subsets[i][:]
                curr_sub.append(num)
                subsets.append(curr_sub)
        return subsets
