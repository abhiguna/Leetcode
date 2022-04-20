class Solution:
    def two_sum(self, nums, i, res):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            curr_sum = nums[i] + nums[j] + nums[k]
            if curr_sum < 0:
                j += 1
            elif curr_sum > 0:
                k -= 1
            else:
                # Found a triplet
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                # Skip duplicates
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                
                k -= 1
                # Skip dups.
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
        return
    
    # Time = O(N^2)
    # Space = O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        res = []
        for i in range(N - 2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            self.two_sum(nums, i, res)
        
        return res