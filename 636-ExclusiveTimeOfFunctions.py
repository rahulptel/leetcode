from collections import deque

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = [0] * n
        stack = deque()
        prev_time = 0
        
        for log in logs:
            id, status, step =  list(log.split(":"))
            id, step = int(id), int(step)            
            # push
            if "s" == status[0]:
                if len(stack):                    
                    times[stack[-1]] += step - prev_time                
                stack.append(id)
                prev_time=step
            # pop
            else:                
                stack.pop()
                times[id] += step - prev_time + 1                
                prev_time=step+1
            
        return times
