class Solution:
    # Time = O(T*2^N)
    # Space = O(T)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        T = target
        res = []
        
        def helper(idx, combination, target_left):
            # Base case
            if target_left == 0:
                res.append(combination[:])
                return
            
            if idx == N or target_left < 0:
                return
            
            # Recursive Case
            count = target_left // candidates[idx]
            
            # Exclude case
            helper(idx+1, combination, target_left)
            
            # Include case
            for i in range(1, count+1):
                for j in range(1, i+1):
                    combination.append(candidates[idx])
                    target_left -= candidates[idx]
                helper(idx+1, combination, target_left)
                for j in range(1, i+1):
                    combination.pop()
                    target_left += candidates[idx]
                    
            return
        
        helper(0, [], target)
        return res