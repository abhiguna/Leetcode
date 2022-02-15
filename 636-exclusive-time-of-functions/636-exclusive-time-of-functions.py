class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0]*n
        stack = []
        prev_time = 0
        
        for log in logs:
            item = log.split(":")
            func_id = int(item[0])
            action = item[1]
            curr_time = int(item[2])
            
            if action == "start":
                if stack:
                    times[stack[-1]] += curr_time - prev_time
                stack.append(func_id)
                prev_time = curr_time
            else:
                times[stack.pop()] += curr_time - prev_time + 1
                prev_time = curr_time + 1
        return times