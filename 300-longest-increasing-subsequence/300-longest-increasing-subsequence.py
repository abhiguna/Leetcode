# Note: This method does not generate a valid subsequence because it violates the order of the elements
#.  But, it will correctly generate the length of the longest subsequence as the len only increases when n > sub[-1]
class Solution:
    # Time = O(nlogn)
    # Space = O(1)
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize a subsequence array
        # We will also keep track of the largest len seen so far
        sub = []
        max_len = 0
        
        # Iterate through every element n in the array
        for n in nums:
            # If sub empty or n > sub[-1] -> add it to the end of sub array
            if len(sub) == 0 or n > sub[-1]:
                sub.append(n)
                max_len = max(max_len, len(sub))
            # Otherwise, replace n with the first element greater than n in the sub array
            else:
                start = 0
                end = len(sub) - 1
                while start <= end:
                    mid = start + (end-start) // 2
                    if sub[mid] < n:
                        start = mid + 1
                    else:
                        end = mid - 1
                sub[start] = n  
        # Return max_len
        return max_len
        

