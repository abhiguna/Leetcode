class Solution:
    # Time = O(N)
    # Space = O(N)
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        # Edge case: N < 2
        if N < 2:
            return False
        
        # Special case: k == 0
        if k == 0:
            for i in range(1, N):
                if nums[i-1] == 0 and nums[i] == 0:
                    return True
            return False
        
        # General case
        hmap = {}
        hmap[0] = True
        
        prefix_sum = nums[0]
        for i in range(1, N):
            old_sum = prefix_sum
            prefix_sum = (prefix_sum + nums[i]) % k
            
            if prefix_sum in hmap:
                return True
            
            # Update hmap by inserting the old prefix sum to ensure a subarray of size 2 exists
            hmap[old_sum % k] = True
        
        # No subarray sum is a multiple of k
        return False