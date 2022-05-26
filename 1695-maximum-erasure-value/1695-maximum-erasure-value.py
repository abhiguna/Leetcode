class Solution:
    # Time = O(N)
    # Space = O(N)
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        window_sum = 0
        max_sum = 0
        left = 0
        hmap = defaultdict(int)
        
        for i in range(N):
            window_sum += nums[i]
            hmap[nums[i]] += 1
            
            while left <= i and hmap[nums[i]] > 1:
                window_sum -= nums[left]
                hmap[nums[left]] -= 1
                if hmap[nums[left]] == 0:
                    del hmap[nums[left]]
                left += 1
            
            max_sum = max(max_sum, window_sum)
        
        return max_sum
            
            