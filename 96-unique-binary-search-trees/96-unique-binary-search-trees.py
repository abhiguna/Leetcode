class Solution:
    
    def numTrees(self, n: int) -> int:
        
        mem = defaultdict(int)
        
        def count_bsts(n):
            nonlocal mem
            
            if n in mem:
                return mem[n]
            
            # Base case
            if n == 0 or n == 1:
                mem[n] = 1
                return 1
            
            # Recursive case
            total_bsts = 0
            for i in range(0, n):
                left_subtree = count_bsts(i)
                right_subtree = count_bsts(n - 1 - i)
                total_bsts += left_subtree * right_subtree
            
            mem[n] = total_bsts
            return total_bsts
        
        return count_bsts(n)
        