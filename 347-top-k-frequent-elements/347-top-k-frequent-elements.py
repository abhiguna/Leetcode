class Solution:
    # Time = O(N) amortized time
    # Space = O(1)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter(nums)
        nums = [(num, freq) for (num, freq) in hmap.items()]
        
        def helper(start, end):
            if start >= end:
                return
            
            pivot_idx = random.randint(start, end)
            (nums[pivot_idx], nums[start]) = (nums[start], nums[pivot_idx])
            pivot = nums[start][1]
            # Lomuto's partitioning 
            left = start
            for right in range(start+1, end+1):
                if nums[right][1] <= pivot:
                    left += 1
                    (nums[left], nums[right]) = (nums[right], nums[left])
            
            (nums[start], nums[left]) = (nums[left], nums[start])
            
            if left == len(nums) - k:
                return
            elif left < len(nums) - k:
                return helper(left+1, end)
            else:
                return helper(start, left-1)
            
        helper(0, len(nums)-1)
        # Update nums
        for i in range(len(nums)-k, len(nums)):
            nums[i] = nums[i][0]
        
        return nums[len(nums)-k:]
        
        
        