class Solution:
    # Time = O(NlogM)
    # Space = O(1)
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        # We do a bisection search on a range of max-distance values
        N = len(stations)
        start = 0
        end = 0
        for i in range(N-1):
            # Calculate max-distance
            end = max(end, stations[i+1] - stations[i])
        
        tolerance = 10 ** (-6)
        while start <= end - tolerance:
            mid = start + (end-start) / 2
            # Boundary: > k stations need | <= k stations needed
            num_stations = 0
            for i in range(N-1):
                num_stations += math.floor((stations[i+1] - stations[i]) / mid)
            
            if num_stations > k:
                # start = mid because of bisection search operates on a continuous range
                start = mid
            else:
                end = mid
        
        return start