class Solution:
    # Time = O(N)
    # Space = O(N)
    def findMaxLength(self, nums: List[int]) -> int:
        N = len(nums)
        
        # The hmap stores the excess values of 0 or 1
        hmap = {}
        hmap[0] = 0
        imbalance = 0
        global_max = 0
        
        for i in range(N):
            # Update current_im
            if nums[i] == 1:
                imbalance += 1
            else:
                imbalance -= 1
            
            curr_len = i + 1
            # Update global_max if imabalance already exists in the hmap
            # By subtracting the shortest len of the imabalance, we get the longest subarray with NO imbalance
            if imbalance in hmap:
                imbalance_len = hmap[imbalance]
                global_max = max(global_max, curr_len - imbalance_len)
            
            # Update hmap
            if imbalance not in hmap:
                hmap[imbalance] = curr_len
        
        return global_max