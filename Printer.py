from collections import deque 

printer_queue = deque()

printer_queue.append('Doc1')
printer_queue.append('Doc2')
printer_queue.append('Pic1')

while printer_queue: 
    job = printer_queue.popleft()
    print(f'Currently printing: {job}')