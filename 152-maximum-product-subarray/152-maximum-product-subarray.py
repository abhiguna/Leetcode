class Solution:
    # Time = O(N)
    # Space = O(1)
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) # 0 -> [-1]
        curr_min, curr_max = 1, 1
        
        for n in nums:
            if n == 0:
                curr_min, curr_max = 1, 1
                continue
            
            temp = curr_max
            curr_max = max(n*curr_max, n*curr_min, n)
            curr_min = min(n*temp, n*curr_min, n)
            res = max(res, curr_max)
        
        return res
            