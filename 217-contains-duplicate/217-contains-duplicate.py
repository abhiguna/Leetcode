class Solution:

    # Time = O(N)
    # Space = O(N)
    def containsDuplicate(self, nums: List[int]) -> bool:
        N = len(nums)
        nums_seen = set()
        
        for i in range(N):
            if nums[i] in nums_seen:
                return True
            
            nums_seen.add(nums[i])
    
        return False
        