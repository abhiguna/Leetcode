class Solution:
    # Time = O(N)
    # Space = O(N)
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = 0
        # For the ith number, divide the boundary as follows:
        #    > k | = k | < k
        #.      ge     le        => # subarrays at idx i is le - ge
        hmap_le = defaultdict(int)
        left_le = 0
        hmap_ge = defaultdict(int)
        left_ge = 0
        
        for i in range(N):
            hmap_le[nums[i]] += 1
            
            while left_le <= i and len(hmap_le) >= k:
                hmap_le[nums[left_le]] -= 1
                if hmap_le[nums[left_le]] == 0:
                    del hmap_le[nums[left_le]]
                left_le += 1
            
            hmap_ge[nums[i]] += 1
            
            while left_ge <= i and len(hmap_ge) > k:
                hmap_ge[nums[left_ge]] -= 1
                if hmap_ge[nums[left_ge]] == 0:
                    del hmap_ge[nums[left_ge]]
                left_ge += 1
            
            count += left_le - left_ge
            
        return count