# Queue using two stacks
from collections import deque

q = int(input())

queue = deque()

for _ in range(q):

    query = list(map(int, input().split()))

    # Enqueue
    if query[0] == 1:
        queue.append(query[1])

    # Dequeue
    elif query[0] == 2:
        queue.popleft()

    # Print front element
    elif query[0] == 3:
        print(queue[0])