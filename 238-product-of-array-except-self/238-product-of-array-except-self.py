# Optimal Solution
class Solution:
    # Pattern: left-right
    # Time = O(n), Space = O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        answer = [0 for _ in range(N)]
        answer[0] = 1
        
        for i in range(1, N):
            answer[i] = answer[i-1] * nums[i-1]
        suffix = 1
        
        for i in range(N-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
            
        return answer
        
        
        