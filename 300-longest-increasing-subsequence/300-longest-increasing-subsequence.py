import bisect

class Solution:
    
    # Time = O(NlogN)
    # Space = O(N)
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        
        subsequence = []
        
        for num in nums:
            idx = bisect.bisect_left(subsequence, num)
            
            # If num is greater than all the numbers in the subsequence, add it
            if idx == len(subsequence):
                subsequence.append(num)
            # Replace it with the first element that is greater than num
            else:
                subsequence[idx] = num
        
        return len(subsequence)