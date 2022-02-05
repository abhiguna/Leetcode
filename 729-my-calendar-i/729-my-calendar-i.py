from sortedcontainers import SortedDict
import bisect

# Time = O(nlogn)
# Space = O(n)
class MyCalendar:
    def __init__(self):
        self.calendar = SortedDict()

    def book(self, start: int, end: int) -> bool:
        start_vals = self.calendar.keys()
        end_vals = self.calendar.values()
        idx = bisect.bisect_left(start_vals, start)
        if (idx == 0 or end_vals[idx-1] <= start) and (idx == len(start_vals) or end <= start_vals[idx]):
            self.calendar[start] = end
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)