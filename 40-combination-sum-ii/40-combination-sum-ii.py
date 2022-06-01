class Solution:
    # Time = O(N*2^N)
    # Space = O(N)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        N = len(candidates)
        res = []
        
        def helper(idx, target_left, slate):
            # Backtracking case
            if target_left < 0 or (idx == N and target_left != 0):
                return
            elif target_left == 0:
                res.append(slate[:])
                return
            else:
                dup = idx
                while dup < N-1 and candidates[dup] == candidates[dup+1]:
                    dup += 1
                
                # Exclude the current element
                helper(dup+1, target_left, slate)
                
                # Include the current element
                slate.append(candidates[idx])
                target_left -= candidates[idx]
                helper(idx+1, target_left, slate)
                slate.pop()
                target_left += candidates[idx]
                return
        
        # Root manager
        helper(0, target, [])
        return res