from heapq import *

class Solution:
    # Time = O(NlogN)
    # Space = O(N)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort(key = lambda x: x[0])
        min_heap = []
        min_rooms = 0
        
        for i in range(N):
            if i == N - 1:
                next_start = float("inf")
            else:
                next_start = intervals[i+1][0]
            
            # Start
            heappush(min_heap, intervals[i][1])
            min_rooms = max(min_rooms, len(min_heap))
            
            # End 
            while min_heap and min_heap[0] <= next_start:
                heappop(min_heap)
        
        return min_rooms