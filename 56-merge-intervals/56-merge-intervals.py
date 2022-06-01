class Solution:
    # Time = O(NlogN)
    # Space = O(1)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        N = len(intervals)
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        res = [intervals[0]]
        
        for i in range(1, N):
            # We have an overlap
            if intervals[i][0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
            # No overlap
            else:
                res.append(intervals[i])
        
        return res
                