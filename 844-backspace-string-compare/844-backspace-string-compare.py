class Solution:
    # Time = O(M + N)
    # Space = O(M + N)
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        
        def compute_final_str(test_str):
            N = len(test_str)
            read, write = 0, 0
            while read < N:
                # Backspace
                if test_str[read] == "#" and write > 0:
                    write -= 1
                # Normal character
                elif test_str[read] != "#":
                    test_str[write] = test_str[read]
                    write += 1
                read += 1
            return test_str[:write]
        
        return (compute_final_str(s) == compute_final_str(t))
        
        
        
        