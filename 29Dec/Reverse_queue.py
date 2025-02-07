from queue import Queue

def reverse_first_k_elements(queue, k):
    if queue.qsize() < k or k <= 0:
        print("Invalid value of k")
        return

    stack = []

    # Step 1: Push the first k elements into the stack
    for _ in range(k):
        stack.append(queue.get())

    # Step 2: Enqueue the stack elements back to the queue
    while stack:
        queue.put(stack.pop())

    # Step 3: Move the remaining elements to the back of the queue
    for _ in range(queue.qsize() - k):
        queue.put(queue.get())

    print("Queue after reversing first", k, "elements:", list(queue.queue))

# Example usage
q = Queue()
for i in range(1, 6):
    q.put(i)

print("Original queue:", list(q.queue))
reverse_first_k_elements(q, 3)
