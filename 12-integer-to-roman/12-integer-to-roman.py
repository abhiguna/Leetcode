class Solution:
    # 58 -> L
    def intToRoman(self, num: int) -> str:
        rom_dict = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        
        rom_arr = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        
        rom_str = []
        divisor = len(rom_arr) - 1
        
        while num != 0:
            while divisor >= 0 and num // (rom_dict[rom_arr[divisor]]) == 0:
                divisor -= 1
            while num // (rom_dict[rom_arr[divisor]]) != 0:
                rom_str.append(rom_arr[divisor])
                num -= rom_dict[rom_arr[divisor]]
            num %= rom_dict[rom_arr[divisor]]
        return ''.join(rom_str)