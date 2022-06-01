class Solution:
    # Time = O(N*2^N)
    # Space = O(N)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Subsets can be reduced to the combinations problem
        res = []
        N = len(nums)
        
        def helper(idx, slate):
            # Base case
            if idx == N:
                res.append(slate[:])
            else:
                # Exclude the current element
                helper(idx+1, slate)
                
                # Include the current element
                slate.append(nums[idx])
                helper(idx+1, slate)
                slate.pop()
            
            return
        
        # Root manager
        helper(0, [])
        return res