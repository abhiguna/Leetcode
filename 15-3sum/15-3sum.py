class Solution:
    # Time = O(N^2)
    # Space = O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        # Edge case
        if N <= 2:
            return []
        
        nums.sort()
        res = []
        
        def find_pair(first, target, start, end):
            j = start
            k = end
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    # Found target
                    res.append([first, nums[j], nums[k]])
                    
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
            return
        
        
        for i in range(N-2):
            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            find_pair(nums[i], -nums[i], i+1, N-1)
        
        return res