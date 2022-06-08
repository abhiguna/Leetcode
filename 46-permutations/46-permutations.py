class Solution:
    # Time = O(N*N!)
    # Space = O(N)
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        N = len(nums)
        
        def helper(fixed_idx):
            # Base case
            if fixed_idx == N:
                res.append(nums[:])
                return
            
            # Recursive case
            for i in range(fixed_idx, N):
                # Swap
                (nums[i], nums[fixed_idx]) = (nums[fixed_idx], nums[i])
                helper(fixed_idx + 1)
                # Unswap
                (nums[i], nums[fixed_idx]) = (nums[fixed_idx], nums[i])
            
            return
        
        helper(0)
        return res