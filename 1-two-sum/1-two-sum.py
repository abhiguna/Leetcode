class Solution:
    # Time = O(N)
    # Space = O(N)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {nums[0]:0}
        N = len(nums)
        
        for i in range(1, N):
            # Found target value
            if target - nums[i] in hmap:
                return [hmap[target-nums[i]], i]
            # Not found the target value
            else:
                hmap[nums[i]] = i
        
        return [-1, -1]
            