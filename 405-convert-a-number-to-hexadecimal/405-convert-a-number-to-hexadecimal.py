class Solution:
    # Time = O(1)
    # Space = O(1)
    def toHex(self, num: int) -> str:
        hmap = {
            0: "0",
            1: "1",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "a",
            11: "b",
            12: "c",
            13: "d",
            14: "e",
            15: "f"
        }
        
        res = deque()
        
        # Since we have a 32 bit number, we will have at most 8 hex digits
        # 15 = 1111 => highest hex value
        for i in range(8):
            res.appendleft(hmap[num & 15])
            # Right shift by 4
            num = num >> 4
            if num == 0:
                break
        
        return "".join(res)
            