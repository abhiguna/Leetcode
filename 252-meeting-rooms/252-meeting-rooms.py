class Solution:
    # Time = O(nlogn)
    # Space = O(1)
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        
        # Edge case: n == 0 -> no overlap
        if n == 0:
            return True
        
        intervals.sort(key=lambda x: x[0]) # O(nlogn)
        
        prev_interval = intervals[0]
        
        for i in range(1, n): # O(n)
            # Overlap
            if intervals[i][0] < prev_interval[1]:
                return False
            elif intervals[i][1] >= prev_interval[1]:
                prev_interval = intervals[i]
        
        return True
                