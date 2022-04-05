class Solution:
    
    # If nums is not cyclical
    def helper(self, nums):
        rob1 = 0
        rob2 = 0
        
        for num in nums:
            new_rob = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = new_rob
        
        return rob2
    
    # Time = O(N)
    # Space = O(1)
    def rob(self, nums: List[int]) -> int:
        # Special case: if given one element long array, max = nums[0]
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))