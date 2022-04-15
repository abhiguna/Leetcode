class Solution:
    # Time = O(NlogN)
    # Space = O(N)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        N = len(intervals)
        intervals.sort(key=lambda x : x[0])
        result = [intervals[0]]
        
        for i in range(1, N):
            # Check overlap
            if result[-1][1] >= intervals[i][0]:
                result[-1] = [result[-1][0], max(result[-1][1], intervals[i][1])]
            # No overlap
            else:
                result.append(intervals[i])
        
        return result