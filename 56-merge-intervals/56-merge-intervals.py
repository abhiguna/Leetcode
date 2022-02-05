class Solution:
    # Time = O(nlogn), Space = O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=lambda time: time[0])
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        i = 1
        N = len(intervals)
        merged = []
        while i < N:
            if intervals[i][0] <= curr_end:
                curr_end = max(curr_end, intervals[i][1])
            else:
                merged.append([curr_start, curr_end])
                curr_start = intervals[i][0]
                curr_end = intervals[i][1]
            if i == N - 1:
                merged.append([curr_start, curr_end])   
            i += 1
        return merged