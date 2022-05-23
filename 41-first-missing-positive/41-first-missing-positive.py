class Solution:
    # Time = O(N)
    # Space = O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        
        # Cycle sort
        for i in range(N):
            while nums[i] != i + 1:
                dest = nums[i] - 1
                if 0 <= dest < N - 1 and nums[dest] != nums[i]:
                    # Swap
                    nums[i], nums[dest] = nums[dest], nums[i]
                else:
                    break
        
        # Find the first missing positive number
        for i in range(N):
            if nums[i] != i + 1:
                return i + 1
        
        # All the first 1,...,N found in the input array, then first missing positive number is N + 1
        return N + 1