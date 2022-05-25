class Solution:
    # Time = O(N)
    # Space = O(1)
    def numOfSubarrays(self, arr: List[int]) -> int:
        N = len(arr)
        MOD = (10 ** 9) + 7
        hmap = {}
        hmap["even"] = 1 # prefix_sum of 0 is even, so there is at least 1 prefix_sum that is even
        hmap["odd"] = 0
        
        total = 0
        prefix_sum = 0
        # To get an odd subarray sum, we can get even_prefix + odd_suffix_from_i or odd_prefix + even_suffix_from_i
        for i in range(N):
            prefix_sum += arr[i]
            
            # Prefix sum is even
            if prefix_sum % 2 == 0:
                total += hmap["odd"]
            # Prefix sum is odd
            else:
                total += hmap["even"]
            
            # Update hmap
            # Prefix sum is even
            if prefix_sum % 2 == 0:
                hmap["even"] += 1
            # Prefix sum is odd
            else:
                hmap["odd"] += 1
        
        return total % MOD