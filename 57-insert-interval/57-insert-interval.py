class Solution:
    # Time = O(N)
    # Space = O(1)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        # Edge case: N == 0
        if N == 0:
            return [newInterval]
        
        res = []
        
        i = 0
        # Skip all the events that end before the newInterval
        while i < N and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        # Overlapping intervals
        while i < N and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        res.append(newInterval)
        
        # Add the remaining elements
        while i < N:
            res.append(intervals[i])
            i += 1
        
        return res
        