class Solution:
    # Time = O(nlogn)
    # Space = O(1)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        
        # Edge case: n == 0
        if n == 0:
            return True
        
        # Sort by start time
        intervals.sort(key = lambda x: x[0])
        
        prev_interval = intervals[0]
        
        for i in range(1, n):
            # Check overlap
            if intervals[i][0] < prev_interval[1]:
                return False
            
            prev_interval[1] = max(prev_interval[1], intervals[i][1])
        
        return True