class Solution:
    # Time = O(logN)
    # Space = O(1)
    def square_sum(self, num):
        total = 0
        while num > 0:
            digit = num % 10
            total += (digit ** 2)
            num = num // 10
        return total
    
    def isHappy(self, n: int) -> bool:
        # Edge case: if n == 1
        if n == 1: return True
        
        hare, tortoise = n, n
        while True:
            hare = self.square_sum(self.square_sum(hare))
            tortoise = self.square_sum(tortoise)
            if hare == tortoise:
                return (tortoise == 1)
        
        return False
            