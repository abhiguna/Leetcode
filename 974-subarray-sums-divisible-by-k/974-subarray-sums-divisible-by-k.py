class Solution:
    # Time = O(N), N: len(nums)
    # Space = O(N)
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Use a hmap<remainder, subarray count>
        prefix_sum = 0
        hmap = defaultdict(int)
        # There is one subarray with remainder of 0
        hmap[0] = 1
        total_count = 0
        
        for n in nums:
            prefix_sum = (prefix_sum + n) % k
            total_count += hmap[prefix_sum]
            hmap[prefix_sum] += 1
        
        return total_count
        