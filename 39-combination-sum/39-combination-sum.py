class Solution:
    # Time = O(n*T^n), T: target
    # Space = O(max(n, T))
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        
        def helper(idx, target_left, slate):
            # Backtracking case
            if target_left < 0:
                return
            # Base cases
            if target_left == 0:
                res.append(slate[:])
                return
            if idx == n:
                if target_left == 0:
                    res.append(slate[:])
                return
            
            # General case
            count = target_left // candidates[idx]
            
            # Exclude case
            helper(idx + 1, target_left, slate)
            
            # Include case
            for i in range(1, count+1):
                slate.append(candidates[idx])
                target_left -= candidates[idx]
                helper(idx+1, target_left, slate)
            
            for i in range(count):
                slate.pop()
                target_left += candidates[idx]
        
        helper(0, target, [])
        return res
        
        