class Solution:
    # Approach: Two-pointer approach
    
    # Time = O(N)
    # Space = O(1)
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        i = 0
        j = N - 1
        # str of len 0 and 1 -> is a palindrome
        while i < j:
            # Skip all non-alphanumeric chars
            if not s[i].isdigit() and not s[i].isalpha():
                i += 1
            elif not s[j].isdigit() and not s[j].isalpha():
                j -= 1
            else:
                # We compare alphanumeric characters
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
        
        return True