class Solution:
    # Time = O(N^2)
    # Space = O(1)
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        # We know a palindrome can either be of odd length or even length
        max_len = 0
        pal_start, pal_end = -1, -1
        
        # We consider each idx in the s as the middle and expand in both directions
        for i in range(N):
            # Find the odd length
            left, right = i, i
            while left >= 0 and right < N and s[left] == s[right]:
                # Check if curr_len > max_len
                if right-left+1 > max_len:
                    max_len = right-left+1
                    pal_start = left
                    pal_end = right
                left -= 1
                right += 1
            
            # Find the even length
            left, right = i, i+1
            while left >= 0 and right < N and s[left] == s[right]:
                # Check if curr_len > max_len
                if right-left+1 > max_len:
                    max_len = right-left+1
                    pal_start = left
                    pal_end = right
                left -= 1
                right += 1
            
        return s[pal_start:pal_end+1]
        
        