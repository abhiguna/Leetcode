class Solution:
    # Time = O(N)
    # Space = O(1)
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        majority = nums[0]
        count = 1
        
        for i in range(1, N):
            if nums[i] == majority:
                count += 1
            else:
                count -= 1
                if count < 0:
                    majority = nums[i]
                    count = 1
        
        return majority