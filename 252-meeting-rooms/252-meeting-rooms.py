class Solution:
    
    # Time = O(NlogN)
    # Space = O(N)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) == 0:
            return True
        
        N = len(intervals)
        intervals.sort(key = lambda x: x[0])
        
        for i in range(1, N):
            overlap = intervals[i][0] >= intervals[i-1][0] and intervals[i][0] < intervals[i-1][1]
            
            if overlap:
                return False
            
        return True