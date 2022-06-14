class Solution:
    # Time = O(n), n: len(nums)
    # Space = O(n)
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        prefix_map = {0: -1} # Stores the diff # 1s - # 0s in the prefix_map
        max_len = 0
        
        for (idx, num) in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1
            
            if count in prefix_map:
                max_len = max(max_len, idx - prefix_map[count])
            else:
                prefix_map[count] = idx
        
        return max_len
        
        
        
"""
Dry run:
nums = [0, 1, 1, 0]

{
    -1: 0
     0: 3
     1: 2
}

nums = [0, 1, 0]
{
    0: -1
    -1: 0
    0: 1
}

"""
        