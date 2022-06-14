class Solution:
    # Time = O(1) -> fixed length of bits (i.e. at most 32-bits given for a number)
    # Space = O(1)
    def hammingWeight(self, n: int) -> int:
        num_ones = 0
        num = n
        while num != 0:
            num = num & (num-1)
            num_ones += 1
        return num_ones
        