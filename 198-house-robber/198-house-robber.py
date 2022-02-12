class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        no_rob = 0
        rob = nums[0]
        for i in range(1, N):
            prev_rob = rob
            rob = nums[i] + no_rob
            no_rob = max(no_rob, prev_rob)
        return max(rob, no_rob)
    
    
        