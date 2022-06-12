class Solution:
    # Time = O(n)
    # Space = O(n)
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        # Edge case: empty array
        if n == 0:
            return 0
        
        nums_set = set(nums)
        max_len = 1
        seq = {} # seq<start_num, len> stores the len of the sequence starting at start_num
        
        for num in nums:
            # Skip if not the start_num or if len of sequence already computed
            if (num-1 in nums_set) or (num in seq):
                continue
            
            seq[num] = 1
            nxt = num + 1
            while nxt in nums_set:
                seq[num] += 1
                max_len = max(max_len, seq[num])
                nxt = nxt + 1
        
        return max_len
                