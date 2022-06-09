class Solution:
    # Time = O(N*2^N)
    # Space = O(N)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        
        def helper(idx, slate):
            # Base case
            if idx == N:
                res.append(slate[:])
                return

            # Exclude case
            helper(idx+1, slate)
            
            # Include case
            slate.append(nums[idx])
            helper(idx+1, slate)
            slate.pop()
            return
            
        helper(0, [])
        return res