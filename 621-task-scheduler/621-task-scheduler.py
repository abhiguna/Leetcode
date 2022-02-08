class Solution:
    # Time = O(m*n), m = len(tasks) and n = idle time
    # Space = O(m)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # each task 1 unit time
        # minimize idle time
        
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap)
        
        curr_time = 0
        queue = deque() # contains pair of values [-cnt, idleTime]
        while max_heap or queue:
            curr_time += 1
            
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    queue.append([cnt, curr_time + n])
            
            if queue and queue[0][1] == curr_time:
                heapq.heappush(max_heap, queue.popleft()[0])
        
        return curr_time
                
        