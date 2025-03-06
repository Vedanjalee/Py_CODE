from collections import deque

def generateBinaryNumbers(n):
    queue = deque()
    queue.append("1")
    result = []

    for _ in range(n):
        num = queue.popleft()
        result.append(num)
        queue.append(num + "0")
        queue.append(num + "1")

    return result

print(generateBinaryNumbers(5))  # Output: ['1', '10', '11', '100', '101']
