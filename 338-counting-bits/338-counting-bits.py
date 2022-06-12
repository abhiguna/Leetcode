class Solution:
    # Time = O(n)
    # Space = O(1)
    def countBits(self, n: int) -> List[int]:
        table = [0] * (n+1)
        curr_offset = 1
        
        for i in range(1, n+1):
            # Update the curr_offset based on i value
            if i == curr_offset * 2: # i.e. powers of 2: 2, 4, 8, 16, ...
                curr_offset = curr_offset * 2
            
            table[i] = 1 + table[i-curr_offset]
        
        return table
        