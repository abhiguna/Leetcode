class Solution:
    # Time = O(1)
    # Space = O(1)
    def intToRoman(self, num: int) -> str:
        table = [
                (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), 
                 (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), 
                 (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
                ]
        N = len(table)
        res = []
        
        for i in range(N):
            # Look at the ith pair & bite off that value as many times needed
            # table[i][0] = value, table[i][1] = symbol
            if num >= table[i][0]:
                q = num // table[i][0]
                res.append(table[i][1]*q)
                num = num % table[i][0]
        
        return "".join(res)