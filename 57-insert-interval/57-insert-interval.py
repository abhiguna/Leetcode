class Solution:
    # Time = O(N)
    # Space = O(1)
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        result = []
        i = 0
        
        # Intervals before -> no overlap
        while i < N and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        
        # Overlap
        while i < N and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        result.append(newInterval)
        
        # Intervals after -> no overlap
        while i < N:
            result.append(intervals[i])
            i += 1
        
        return result