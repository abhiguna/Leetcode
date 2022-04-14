from heapq import *

class Solution:
    # Time = O(NlogN)
    # Space = O(N)
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        N = len(trips)
        min_heap = []
        total_passengers = 0
        
        for i in range(N):
            if i == N - 1:
                next_start = float("inf")
            else:
                next_start = trips[i+1][1]
            
            # Start a new trip
            heappush(min_heap, (trips[i][2], trips[i][0]))
            total_passengers += trips[i][0]
            if total_passengers > capacity:
                return False
            
            # End the previous trip
            while min_heap and min_heap[0][0] <= next_start:
                end_time, pass_count = heappop(min_heap)
                total_passengers -= pass_count
        
        return True
            