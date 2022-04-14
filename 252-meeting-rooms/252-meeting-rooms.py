class Solution:
    
    # Time = O(NlogN)
    # Space = O(N)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        N = len(intervals)
        if N == 0:
            return True
        
        intervals.sort(key=lambda x: x[0])
        for i in range(N):
            if i == N - 1:
                next_start = float("inf")
            else:
                next_start = intervals[i+1][0]
            
            # Overlap
            if intervals[i][1] > next_start:
                return False
            
        return True