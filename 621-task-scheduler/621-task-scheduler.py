from heapq import *
from collections import *

class Solution:
    # Time = O(N)
    # Space = O(1)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        # Insert values of each char into the max_heap
        max_heap = [ -cnt for cnt in task_count.values()]
        heapify(max_heap)
        
        # Task queue keeps track of tasks to be processed (-cnt, ready_time)
        task_queue = deque()
        # Holds the current time
        timestamp = 0
        
        while max_heap or task_queue:
            timestamp += 1
            
            if max_heap:
                cnt = heappop(max_heap)
                # Update cnt -> one less instance available for future use
                cnt = -1*(abs(cnt) - 1)
                # Add to the queue if at least one instance is available
                if cnt != 0:
                    task_queue.append((cnt, timestamp + n))
                
            # Process if a task is ready
            if task_queue and task_queue[0][1] == timestamp:
                (cnt, ready_time) = task_queue.popleft()
                heappush(max_heap, cnt)
        
        return timestamp
                