class Solution:
    # Time = O(n*n!)
    # Space = O(n)
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def helper(idx):
            # Base case: idx == n
            if idx == n:
                res.append(nums[:])
                return
            
            for i in range(idx, n):
                # Swap
                nums[i], nums[idx] = nums[idx], nums[i]
                helper(idx+1)
                # Unswap
                nums[i], nums[idx] = nums[idx], nums[i]
        
        helper(0)
        return res