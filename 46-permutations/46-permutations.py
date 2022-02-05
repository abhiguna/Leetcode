class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        # Base case
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            first_num = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(first_num)
                result.append(perm)
            nums.append(first_num)
        return result
    
            