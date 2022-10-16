class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0

    def isfull(self):
        # rear 다음 칸이 front일 때 full 상태로 봄
        return (self.rear + 1) % self.size == self.front

    def isempty(self):
        return self.rear == self.front

    def enqueue(self, item):
        if self.isfull():
            print("Queue is full")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = item

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
