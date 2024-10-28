from collections import deque

queue = deque()

queue.append('Alice')
queue.append('Bob')
queue.append('Charlie')

print(queue)
queue.popleft()
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)
