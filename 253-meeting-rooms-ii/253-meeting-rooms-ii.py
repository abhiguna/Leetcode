from heapq import *
import math

class Solution:
    # Time = O(NlogN)
    # Space = O(N)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        
        N = len(intervals)
        min_heap = []
        min_rooms = 0
        
        for i in range(N):
            if i == N-1:
                next_start = math.inf
            else:
                next_start = intervals[i+1][0]
            
            # Process the current interval
            heappush(min_heap, (intervals[i][1], id(intervals[i][1]), intervals[i]))
            min_rooms = max(min_rooms, len(min_heap))
            
            # End the current interval -> remove all intervals that end before the next event
            while min_heap and min_heap[0][0] <= next_start:
                heappop(min_heap)
        
        return min_rooms
                