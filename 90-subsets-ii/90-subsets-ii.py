class Solution:
    # Time = O(N*2^N)
    # Space = O(N)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        # Sort the current input
        nums.sort()
        res = []
        
        def helper(idx, slate):
            if idx == N:
                res.append(slate[:])
            else:
                # Find the number of times the dup element occurs
                dup = idx
                while dup < N-1 and nums[dup] == nums[dup+1]:
                    dup += 1
                
                # Exclude case
                helper(dup+1, slate)
                
                # Include case
                slate.append(nums[idx])
                helper(idx+1, slate)
                slate.pop()
                return
                
        # Root manager
        helper(0, [])
        return res