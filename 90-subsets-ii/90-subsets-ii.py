class Solution:
    # Time = O(N * 2^N)
    # Space = O(N)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []
        
        def dfs(idx, slate):
            # Base case
            if idx == N:
                res.append(slate[:])
                return
            
            # Recursive case
            count = 0
            for i in range(idx, N):
                if nums[i] != nums[idx]:
                    break
                count += 1
            
            # Exclude case
            dfs(idx + count, slate)
            
            # Include case
            for i in range(count):
                slate.append(nums[idx])
                dfs(idx + count, slate)
            
            # Pop all the elements from the slate
            while count > 0:
                slate.pop()
                count -= 1
            
            return
        
        nums.sort()
        dfs(0, [])
        return res