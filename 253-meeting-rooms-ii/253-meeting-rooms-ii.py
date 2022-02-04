class Solution:
    # Time = O(nlogn)
    # Space = O(n)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        start_times = [time[0] for time in intervals]
        end_times = [time[1] for time in intervals]
        
        start_times.sort()
        end_times.sort()
        
        rooms = 0
        max_rooms = rooms
        start_idx = 0
        end_idx = 0
        
        while start_idx < N:
            if start_times[start_idx] < end_times[end_idx]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                start_idx += 1
            else:
                rooms -= 1
                end_idx += 1
        
        return max_rooms