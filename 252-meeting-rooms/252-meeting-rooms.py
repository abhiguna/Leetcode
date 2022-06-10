class Solution:
    # Time = O(NlogN)
    # Space = O(1)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        N = len(intervals)
        # Edge case: no intervals
        if N == 0:
            return True
        
        intervals.sort(key=lambda x:x[0])
        
        # Interval line sweep
        for i in range(N):
            if i == N-1:
                next_start = math.inf
            else:
                next_start = intervals[i+1][0]
            
            # Check overlap
            if intervals[i][1] > next_start:
                return False
        
        return True