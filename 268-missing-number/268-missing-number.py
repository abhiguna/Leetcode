class Solution:
    # Time = O(N)
    # Space = O(1)
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        # Cycle sort
        for i in range(N):
            while nums[i] != i:
                dest = nums[i]
                if dest != N:
                    # Swap
                    nums[i], nums[dest] = nums[dest], nums[i]
                else:
                    # nums[i] == N
                    break
        
        # Find the missing number
        for i in range(N):
            if nums[i] != i:
                return i
        
        # 0,...,N-1 present in the array and N is missing from the array
        return N