class Solution:
    # Time = O(NlogN)
    # Space = O(N)
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        N = len(startTime)
        
        # Build the intervals list
        intervals = []
        for i in range(N):
            new_interval = [startTime[i], endTime[i], profit[i]]
            intervals.append(new_interval)
        
        # Sort by start and end times
        intervals.sort(key=lambda x: x[0])
        intervals.sort(key=lambda x: x[1])
        
        # Build non_overlapping list
        non_overlapping = [-1 for i in range(N)]
        for i in range(N):
            start = 0
            end = i - 1
            while start <= end:
                mid = start + (end-start) // 2
                
                # Overlap:
                if intervals[mid][1] <= intervals[i][0]:
                    non_overlapping[i] = mid
                    start = mid + 1
                # Non-overlap:
                else:
                    end = mid - 1
        
        profit = {-1: 0}
        
        # Compute max_profit achieved 
        for i in range(N):
            profit[i] = max(profit[i-1], intervals[i][2] + profit[non_overlapping[i]])
        
        return profit[N-1]
        