class Solution:
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
