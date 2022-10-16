class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size        # size만큼 미리 잡아놓기
        self.front = -1                   # 마지막으로 꺼낸 자리
        self.rear = -1                    # 마지막으로 저장한 자리

    def enqueue(self, item):
        if self.isfull():
            print("Queue is full")
        else:
            self.rear += 1
            self.queue[self.rear] = item

    def dequeue(self):
        if self.isempty():
            return "Queue is empty"
        else:
            self.front += 1
            return self.queue[self.front]

    def isempty(self):
        return self.front == self.rear

    def isfull(self):
        return self.rear == self.size - 1

    def peek(self):
        return self.queue[self.front]


q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.queue)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
