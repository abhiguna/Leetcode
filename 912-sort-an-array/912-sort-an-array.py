class Solution:
    # Approach: Quick sort -> in-place
    # Time = O(NlogN) amortized
    # Space = O(1) excluding implicit stack space 
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(start, end):
            # Base case
            if start >= end:
                return
            
            pivot_idx = random.randint(start, end)
            (nums[start], nums[pivot_idx]) = (nums[pivot_idx], nums[start])
            pivot = nums[start]
            
            left = start
            for right in range(start+1, end+1):
                if nums[right] <= pivot:
                    left += 1
                    (nums[left], nums[right]) = (nums[right], nums[left])
            
            (nums[start], nums[left]) = (nums[left], nums[start])
            quicksort(start, left-1)
            quicksort(left+1, end)
            return
            
        quicksort(0, len(nums) - 1)
        return nums