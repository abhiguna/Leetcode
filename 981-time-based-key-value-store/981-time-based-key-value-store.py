class TimeMap:
    def __init__(self):
        self.hmap = defaultdict(list)

    # Time = O(1)
    # Space = O(1)
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key].append((value, timestamp))
        return

    # Time = O(logN)
    # Space = O(1)
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values_list = self.hmap[key]
        
        start = 0
        end = len(values_list) - 1
        while start <= end:
            mid = start + (end-start) // 2
            
            # timestamp at mid <= timestamp input
            if values_list[mid][1] <= timestamp:
                res = values_list[mid][0]
                start = mid + 1
            else:
                end = mid - 1
                
        
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)