class Solution:
    # Time = O(N)
    # Space = O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)
        i = 0
        j = N - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else: # sum > target
                j -= 1
        
        # Will never reach this point -> contains exactly one solution
        return [-1, -1]
                