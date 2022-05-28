class Solution:
    def findComplement(self, num: int) -> int:
        # Find the first highest power of two > num
        num_bits = 0
        num_cpy = num
        while num_cpy != 0:
            num_cpy = num_cpy >> 1
            num_bits += 1
        
        bitmask = (1 << num_bits) - 1
        return num ^ bitmask