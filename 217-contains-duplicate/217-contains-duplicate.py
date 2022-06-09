class Solution:
    # Time = O(N)
    # Space = O(N)
    def containsDuplicate(self, nums: List[int]) -> bool:
        N = len(nums)
        hset = set()
        
        for i in range(N):
            if nums[i] in hset:
                return True
            else:
                hset.add(nums[i])
        
        return False