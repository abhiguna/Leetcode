class Solution:
    # Time = O(NlogN)
    # Space = O(N)
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[1])
        total_passengers = 0
        min_heap = []
        N = len(trips)
        
        for i in range(N):
            if i == N - 1:
                next_start = math.inf
            else:
                next_start = trips[i+1][1]
                
            # Start the current trip
            total_passengers += trips[i][0]
            
            if total_passengers > capacity:
                return False
            
            heappush(min_heap, ((trips[i][2], trips[i][0])))
            
            # End the current trip
            while min_heap and min_heap[0][0] <= next_start:
                end_time, passengers = heappop(min_heap)
                total_passengers -= passengers
                
        return True
            
            