from collections import deque

def interleaveQueue(queue):
    half = len(queue) // 2
    stack = []

    for _ in range(half):
        stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())
    
    for _ in range(half):
        queue.append(queue.popleft())

    for _ in range(half):
        stack.append(queue.popleft())

    while stack:
        queue.append(stack.pop())
        queue.append(queue.popleft())

    return list(queue)

queue = deque([1, 2, 3, 4, 5, 6])
print(interleaveQueue(queue))  # Output: [1, 4, 2, 5, 3, 6]
