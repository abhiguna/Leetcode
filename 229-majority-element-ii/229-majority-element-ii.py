class Solution:
    # Time = O(N)
    # Space = O(1)
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        hmap = {}
        
        # Find the potential majority elements -> there can be at most 2 with count > N/3
        for i in range(N):
            if nums[i] in hmap:
                hmap[nums[i]] += 1
            else:
                if len(hmap) < 2:
                    hmap[nums[i]] = 1
                else:
                    # Decrement all the keys
                    for key in list(hmap):
                        hmap[key] -= 1
                        if hmap[key] == 0:
                            del hmap[key]
        
        # Reset the count of each key in hmap
        for key in list(hmap):
            hmap[key] = 0
        
        # Find the count of each key in the input array
        for i in range(N):
            if nums[i] in hmap:
                hmap[nums[i]] += 1
        
        # Find the final list of majority elements
        res = []
        for key in list(hmap):
            if hmap[key] > N//3:
                res.append(key)
                
        return res