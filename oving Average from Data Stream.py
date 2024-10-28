from collections import deque 

class MovingAverage:
    def __init__(self,size):
        self.queue = deque
        self.size  = size
        self.total = 0

    def calculate_moving_average(self,val):
        if len(self.queue) == self.size:
            self.total -= self.queue.popleft()
        self.queue.append(val)
        self.total += val
        return round(self.total / len(self.queue) , 2)