class Solution:
    # Time = O(logN)
    # Space = O(1)
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # Find the leftmost idx
        N = len(nums)
        start = 0
        end = N - 1
        # < t | >= t
        while start <= end:
            mid = start + (end-start) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        
        # Edge case: If target is not found
        if start == N or nums[start] != target:
            return False
        
        # Find the rightmost idx
        #  <= t | > t
        leftmost_idx = start
        end = N - 1
        while start <= end:
            mid = start + (end-start) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        rightmost_idx = end
        
        # Calculate the diff in len
        # num_elements > N / 2
        sub_len = rightmost_idx - leftmost_idx + 1
        
        # Compute the bool result
        return (sub_len > (N // 2))