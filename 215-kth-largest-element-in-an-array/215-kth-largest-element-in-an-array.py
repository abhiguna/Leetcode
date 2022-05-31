class Solution:
    # Time = O(N), N: len(nums)
    # Space = O(1) explicit aux. space
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def helper(start, end):
            pivot_idx = random.randint(start, end)
            (nums[start], nums[pivot_idx]) = (nums[pivot_idx], nums[start])
            pivot = nums[start]
            
            # Partition
            left = start
            for right in range(start+1, end+1):
                if nums[right] <= pivot:
                    left += 1
                    (nums[left], nums[right]) = (nums[right], nums[left])
            
            # Swap pivot with the left ptr
            (nums[start], nums[left]) = (nums[left], nums[start])
            
            # 3 cases
            if left == len(nums) - k:
                return nums[left]
            elif left < len(nums) - k:
                return helper(left+1, end)
            else:
                return helper(start, left-1)
            
            
        
        kth_largest = helper(0, len(nums) - 1)
        return kth_largest