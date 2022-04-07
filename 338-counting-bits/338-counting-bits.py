class Solution:
    # Time = O(N)
    # Space = O(1)
    def countBits(self, n: int) -> List[int]:
        count = []
        for i in range(n + 1):
            count.append(bin(i).count("1"))
        
        return count