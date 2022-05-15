class Solution:
    # Approach: two-pointer 
    
    # Time = O(N)
    # Space = O(1)
    def validPalindrome(self, s: str) -> bool:
        N = len(s)
        
        def is_palindrome(sub):
            i = 0
            j = len(sub) - 1
            
            while i < j:
                if sub[i] != sub[j]:
                    return False
                else:
                    i += 1
                    j -= 1
            
            return True
        
        i = 0
        j = N - 1
        while i < j:
            if s[i] != s[j]:
                # Delete one char
                return is_palindrome(s[i+1:j+1]) or is_palindrome(s[i:j])
            else:
                i += 1
                j -= 1
        
        return True