from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.items = deque()
        self.running_mean = 0
        
    def next(self, val: int) -> float:
        if len(self.items) >= self.size:
            self.running_mean = ((self.running_mean * self.size) - self.items.popleft() + val) / self.size
        else:
            n_items = len(self.items)
            self.running_mean = ((self.running_mean * n_items) + val) / (n_items + 1)

        self.items.append(val)

        return self.running_mean
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
