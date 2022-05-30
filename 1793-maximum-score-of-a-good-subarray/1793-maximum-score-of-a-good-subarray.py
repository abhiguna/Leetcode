class Solution:
    # Time = O(N)
    # Space = O(1)
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        max_score = nums[k]
        min_height = nums[k]
        i = k - 1
        j = k + 1
        
        while i >= 0 and j < N:
            if nums[i] > nums[j]:
                min_height = min(min_height, nums[i])
                # Update the score using the rectangle from [i, j-1]
                max_score = max(max_score, (j-i) * min_height)
                i -= 1
            else: 
                min_height = min(min_height, nums[j])
                # Update the score using the rectangle from [i+1, j]
                max_score = max(max_score, (j-i) * min_height)
                j += 1
        
        # Gather phase
        while i >= 0:
            min_height = min(min_height, nums[i])
            max_score = max(max_score, (j-i) * min_height)
            i -= 1
        
        while j < N:
            min_height = min(min_height, nums[j])
            # Update the score using the rectangle from [i+1, j]
            max_score = max(max_score, (j-i) * min_height)
            j += 1
        
        return max_score
        
            
                
        