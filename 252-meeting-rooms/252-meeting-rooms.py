class Solution:
    
    # Time = O(NlogN), N: len(intervals)
    # Space = O(N)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Edge case
        if len(intervals) == 0:
            return True
        
        intervals.sort(key=lambda x: x[0])
        for i in range(1, len(intervals)):
            overlap = intervals[i][0] >= intervals[i-1][0] and intervals[i][0] < intervals[i-1][1]
            if overlap:
                return False
        
        return True
        