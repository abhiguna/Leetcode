class Solution:
    # Time = O(N^2)
    # Space = O(1)
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        pal = [""]
        pal_len = [0]
        
        def find_longest_pal(left, right):
            while left >= 0 and right < N and s[left] == s[right]:
                if right-left+1 > pal_len[0]:
                    pal_len[0] = right-left+1
                    pal[0] = s[left:right+1]
                left -= 1
                right += 1
            return
        
        # Consider every idx of the string as the middle element of a palindrome
        for i in range(0, N):
            # Odd len palindrome
            left, right = i, i
            find_longest_pal(left, right)
                
            # Even len palindrome
            left, right = i, i+1
            find_longest_pal(left, right)
        
        return pal[0]