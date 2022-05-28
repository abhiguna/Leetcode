class Solution:
    def hammingWeight(self, n: int) -> int:
        num_ones = 0
        num_cpy = n
        while num_cpy != 0:
            if num_cpy & 1 == 1:
                num_ones += 1
            num_cpy = num_cpy >> 1
        return num_ones