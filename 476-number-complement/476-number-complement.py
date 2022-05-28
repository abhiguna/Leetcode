class Solution:
    def findComplement(self, num: int) -> int:
        # Find the first highest power of two
        high_pow = 0
        while 2**high_pow <= num:
            high_pow += 1
        
        bitmask = (2**high_pow) - 1
        
        return num ^ bitmask