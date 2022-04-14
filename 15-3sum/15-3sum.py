class Solution:
    
    def find_pairs(self, nums, i, N, triplets):
        j = i + 1
        k = N - 1
        while j < k:
            curr_sum = nums[i] + nums[j] + nums[k]
            if curr_sum < 0:
                j += 1
            elif curr_sum > 0:
                k -= 1
            else:
                # Equal
                triplets.append([nums[i], nums[j], nums[k]])
                
                j += 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                    
                k -= 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
        return
    
    # Time = O(N^2)
    # Space = O(N)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        triplets = []
        i = 0
        for i in range(N - 2):
            # Skip duplicates
            if i > 0 and nums[i-1] == nums[i]:
                continue
            
            self.find_pairs(nums, i, N, triplets)
        
        return triplets
            
        