class Solution:
    # Time = O(n*n!), n: len(nums)
    # Space = O(n)
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def helper(idx):
            # Base case:
            if idx == n:
                res.append(nums[:])
                return
            # General case:
            for i in range(idx, n):
                # Swap
                nums[idx], nums[i] = nums[i], nums[idx]
                helper(idx+1)
                # Unswap
                nums[idx], nums[i] = nums[i], nums[idx]
                
        helper(0)
        return res