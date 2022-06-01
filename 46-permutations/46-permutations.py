class Solution:
    # Time = O(N*N!)
    # Space = O(N)
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        
        def helper(anchor_idx):
            # Base case
            if anchor_idx == N:
                res.append(nums[:])
                return
            else:
                for i in range(anchor_idx, N):
                    # Swap with anchor idx
                    (nums[i], nums[anchor_idx]) = (nums[anchor_idx], nums[i])
                    helper(anchor_idx + 1)
                    # Unswap
                    (nums[i], nums[anchor_idx]) = (nums[anchor_idx], nums[i])
                return
        
        # Root manager
        helper(0)
        return res