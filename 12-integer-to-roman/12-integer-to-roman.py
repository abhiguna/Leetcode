class Solution:
    # Pattern: hashmap
    # Time: O(1)
    # Space: O(1)
    def intToRoman(self, num: int) -> str:
        rom_list = [
                    ['I',1], ['IV',4], ['V',5], 
                    ['IX',9], ['X',10], ['XL',40], 
                    ['L',50], ['XC',90], ['C',100], 
                    ['CD',400], ['D',500], ['CM',900], ['M',1000]
                   ]
        
        rom_str = []
        
        for rom, val in reversed(rom_list):
            if num // val:
                count = num // val
                rom_str.append(rom * count)
                num = num % val
        return ''.join(rom_str)