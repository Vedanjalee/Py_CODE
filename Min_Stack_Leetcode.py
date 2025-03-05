class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        if not self.stack:
            return None
        tmp = []
        mini = self.stack[-1]

        while self.stack:
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())

        while tmp:
            self.stack.append(tmp.pop())

        return mini


min_stack = MinStack()

while True:
    command = input("Enter command (push <num>/pop/top/getMin/exit): ").split()
    if command[0] == "push":
        min_stack.push(int(command[1]))
    elif command[0] == "pop":
        min_stack.pop()
    elif command[0] == "top":
        print("Top:", min_stack.top())
    elif command[0] == "getMin":
        print("Min:", min_stack.getMin())
    elif command[0] == "exit":
        break
    else:
        print("Invalid command!")
