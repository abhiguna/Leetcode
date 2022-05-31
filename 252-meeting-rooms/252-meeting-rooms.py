class Solution:
    # Time = O(NlogN)
    # Space = O(N)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        N = len(intervals)
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        for i in range(N):
            if i == N - 1:
                next_start = math.inf
            else:
                next_start = intervals[i+1][0]
            
            if next_start < intervals[i][1]:
                return False
        
        return True