from collections import deque
def interleave_queue(queue):
    half_size = len(queue) // 2
    first_half = deque()
    for _ in range(half_size):
        first_half.append(queue.popleft())

    while first_half: 
        queue.append(first_half.popleft())
        if queue: 
            queue.append(queue.popleft())
    
    return queue