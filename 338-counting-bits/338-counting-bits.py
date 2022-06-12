class Solution:
    # Time = O(N)
    # Space = O(1)
    def countBits(self, n: int) -> List[int]:
        res = []
        for num in range(0, n+1):
            one_bits = 0
            
            while num > 0:
                # chew up at the lsb
                one_bits += (num & 1)
                num = num >> 1
            
            res.append(one_bits)
        
        return res