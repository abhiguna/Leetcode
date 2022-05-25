class Solution:
    # Time = O(N), N: len(nums)
    # Space = O(N)
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Initialize an empty hMap that stores the prefix and the count of the prefix
        hmap = {}
        
        # Base case: there is one prefix
        hmap[0] = 1
        prefix_sum = 0
        total = 0
        
        for n in nums:
            prefix_sum += n
            # Check if diff in hmap and update total # of subarrays accordingly
            if prefix_sum - k in hmap:
                total += hmap[prefix_sum - k]
            
            # Update hmap
            if prefix_sum in hmap:
                hmap[prefix_sum] += 1
            else:
                hmap[prefix_sum] = 1
        
        return total