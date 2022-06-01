"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    # Time = O(Nlogk), N: # of total intervals, k: # of employees
    # Space = O(N)
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        res = [(-math.inf, -math.inf)]
        min_heap = []
        k = len(schedule)
        for eidx in range(k):
            if len(schedule[eidx]) > 0:
                heappush(min_heap, (schedule[eidx][0].start, eidx, 0))
        
        while min_heap:
            (start, eidx, pos) = heappop(min_heap)
            # No overlap
            if res[-1][1] < start:
                res.append((start, schedule[eidx][pos].end))
            else:
                res[-1] = (res[-1][0], max(res[-1][1], schedule[eidx][pos].end))
            
            if pos + 1 < len(schedule[eidx]):
                heappush(min_heap, (schedule[eidx][pos+1].start, eidx, pos+1))
        
        # The list res now contains all the disjoint interval list of employees busy times
        free_times = []
        for i in range(1, len(res)-1):
            free_times.append(Interval(res[i][1], res[i+1][0]))
        
        return free_times
        