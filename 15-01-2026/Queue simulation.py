class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None


if __name__ == "__main__":
    q = QueueUsingStacks()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print(q.dequeue())
    print(q.dequeue())
