"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
from heapq import *
import math

class Solution:
    # Time = O(NlogK), N = Total # of intervals
    # Space = O(N)
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        K = len(schedule)
        min_heap = []
        result = [Interval(-math.inf, -math.inf)]
        
        # Insert first interval of each employee
        for i in range(K):
            if schedule[i]:
                heappush(min_heap, (schedule[i][0].start, i, 0))
        
        # Build result array
        while min_heap:
            curr_start, emp_idx, int_idx = heappop(min_heap)
            if curr_start >= result[-1].end:
                result.append(schedule[emp_idx][int_idx])
            else:
                # Overlap
                result[-1] = Interval(result[-1].start, max(result[-1].end, schedule[emp_idx][int_idx].end))    
            
            int_idx += 1
            if int_idx < len(schedule[emp_idx]):
                heappush(min_heap, (schedule[emp_idx][int_idx].start, emp_idx, int_idx))
            
        # Get the freetimes
        free_times = []
        for i in range(1, len(result) - 1):
            # Free time exists
            if result[i].end < result[i+1].start:
                free_times.append(Interval(result[i].end, result[i+1].start))
        
        return free_times
                