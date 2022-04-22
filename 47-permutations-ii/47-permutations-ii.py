class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        nums.sort()
        
        def dfs(idx):
            # Base case
            if idx == N:
                res.append(nums[:])
                return
            
            already_used = set()
            
            for i in range(idx, N):
                if nums[i] not in already_used:
                    already_used.add(nums[i])
                    # Swap
                    nums[idx], nums[i] = nums[i], nums[idx]
                    dfs(idx + 1)
                    # Swap back
                    nums[idx], nums[i] = nums[i], nums[idx]
            
            return
        
        dfs(0)
        return res