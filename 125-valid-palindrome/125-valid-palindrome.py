class Solution:
    # Time = O(N)
    # Space = O(1)
    def isPalindrome(self, s: str) -> bool:
        N = len(s)
        left = 0
        right = N - 1
        
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                # Not palindromic case
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        
        return True
        