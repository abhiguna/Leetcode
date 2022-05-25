class Solution:
    # Time = O(N)
    # Space = O(N)
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        N = len(nums)
        # Use a hmap<prefix_sum - k><shortest len with prefix_sum - k as its prefix>
        hmap = {}
        hmap[0] = 0
        prefix_sum = 0
        # Stores the length of the longest subarray with sum == k
        global_max = 0
        for i in range(N):
            prefix_sum += nums[i]
            
            # Check if a subarray of sum k exists ending at idx i
            if prefix_sum - k in hmap:
                # Update global_max
                global_max = max(global_max, (i+1) - hmap[prefix_sum - k])
            
            # Update the len of the current prefix if the shortest len does not already exist in the hmap
            if prefix_sum not in hmap:
                hmap[prefix_sum] = i + 1
        
        return global_max