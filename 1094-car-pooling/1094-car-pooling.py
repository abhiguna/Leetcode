class Solution:
    # Time = O(NlogN)
    # Space = O(N)
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        
        N = len(trips)
        min_heap = []
        curr_passengers = 0
        
        for i in range(N):
            if i == N-1:
                next_start = math.inf
            else:
                next_start = trips[i+1][1]
            
            # Process the current event
            curr_passengers += trips[i][0]
            if curr_passengers > capacity:
                return False
            heappush(min_heap, (trips[i][2], trips[i][0]))
            
            
            # Remove all ending events
            while min_heap and min_heap[0][0] <= next_start:
                num_passengers = heappop(min_heap)[1]
                curr_passengers -= num_passengers
                
        
        return True