class Solution:
    # Time = O(1)
    # Space = O(1)
    def numberToWords(self, num: int) -> str:
        # Edge case
        if num == 0:
            return "Zero"
        
        # We consider 3-digits at a time, and append it with the respective suffix [billion, million, thousand, ...]
        suffix = [" Billion", " Million", " Thousand", ""]
        final_res = []
        denominator = 10**9
        
        
        name_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }
        def three_digit_to_name(num):
            hundreds = num // 100
            tens = (num % 100) // 10
            ones = (num % 10)
            
            res = []
            if hundreds > 0:
                res.append(name_map[hundreds] + " Hundred")
            
            if tens == 1:
                res.append(name_map[num % 100])
            else:
                if tens > 0:
                    res.append(name_map[tens*10])
                if ones > 0:
                    res.append(name_map[ones])
            
            return " ".join(res)
            
        
        # We can have at most 4 groupings
        for i in range(4):
            q = num // denominator
            if q > 0:
                final_res.append(three_digit_to_name(q) + suffix[i])
            num = num % denominator
            denominator = denominator // 1000
        
        
        return " ".join(final_res)
        
        
        
        