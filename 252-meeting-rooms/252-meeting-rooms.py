class Solution:
    # Time = O(nlogn)
    # Space = O(1)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        # Edge case: empty intervals
        if n == 0:
            return True
        
        intervals.sort(key=lambda x: x[0])
        prev_interval = intervals[0]
        
        for i in range(1, n):
            # Overlap
            if intervals[i][0] < prev_interval[1]:
                return False
            prev_interval = intervals[i]
        
        # No overlap
        return True