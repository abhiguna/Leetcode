class Solution:
    # Time = O(NlogN)
    # Space = O(N)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        N = len(intervals)
        
        for i in range(N-1):
            next_start = intervals[i+1][0]
            # New interval
            if intervals[i][1] > next_start:
                return False
        
        return True