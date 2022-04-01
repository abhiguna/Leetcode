class Solution:
    
    def two_sum(self, nums, N, i, res):
        j = i + 1
        k = N - 1
        
        while j < k:
            _sum = nums[i] + nums[j] + nums[k]
            
            if _sum < 0:
                j += 1
            elif _sum > 0:
                k -= 1
            else:
                res.append([nums[i], nums[j], nums[k]])
                
                j += 1
                # Prevent duplicates for second ptr
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                
                k -= 1
                # Prevent duplicates for third ptr
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
        
        return res
                
    # Time = O(N^2)
    # Space = O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        
        res = []
        
        for i in range(N - 2):
            # Prevent duplicates for first ptr
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            self.two_sum(nums, N, i, res)
        
        return res