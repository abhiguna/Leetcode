class Solution:
    # Time = O(N)
    # Space = O(1)
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        hmap = {}
        
        for i in range(N):
            if nums[i] in hmap:
                hmap[nums[i]] += 1
            else:
                if len(hmap) < 1:
                    hmap[nums[i]] = 1
                else:
                    for key in list(hmap.keys()):
                        hmap[key] -= 1
                        # Delete the hmap entry if the freq. count becomes 0
                        if hmap[key] == 0:
                            del hmap[key]
        
        # Return the majority element
        majority = -1
        for key in list(hmap.keys()):
            majority = key
        
        return majority
                