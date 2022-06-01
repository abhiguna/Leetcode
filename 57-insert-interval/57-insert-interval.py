class Solution:
    # Time = O(N)
    # Space = O(1)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        res = []
        break_idx = N
        
        # Add all the intervals before the newInterval
        for i in range(N):
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                break_idx = i
                break
        
        res.append(newInterval)
        
        for i in range(break_idx, N):
            if intervals[i][0] <= res[-1][1]:
                res[-1] = [min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])
        
        return res