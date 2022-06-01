class Solution:
    # Time = O(N*2^N)
    # Space = O(N)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        res = []
        candidates.sort()
        
        def helper(idx, target_left, slate):
            # Backtracking case
            if (target_left < 0) or (idx == N and target_left != 0):
                return
            
            # Base case
            if target_left == 0:
                res.append(slate[:])
                return
            
            # General case
            # Exclude
            helper(idx+1, target_left, slate)
            
            # Include
            count = target_left // candidates[idx]
            for i in range(1, count+1):
                for j in range(i):
                    slate.append(candidates[idx])
                    target_left -= candidates[idx]
                helper(idx+1, target_left, slate)
                for j in range(i):
                    slate.pop()
                    target_left += candidates[idx]
    
            return
            
        
        helper(0, target, [])
        return res