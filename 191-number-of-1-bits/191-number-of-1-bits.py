class Solution:
    # Time = O(Q), Q: # of 1 bits
    # Space = O(1)
    def hammingWeight(self, n: int) -> int:
        num_cpy = n
        count = 0
        while num_cpy != 0:
            num_cpy = num_cpy & (num_cpy-1)
            count += 1
        return count
            