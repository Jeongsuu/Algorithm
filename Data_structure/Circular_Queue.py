 # 배열로 구현한 환형 큐

class CircularQueue:

    def __init__(self, n):         # constructor method
        self.maxCount = n          # 인자로 주어진 최대 큐 길이 설정
        self.data = [None] * n     # 배열 초기화
        self.count = 0             # 현재 큐에 들어있는 데이터 개수
        self.front = -1
        self.rear = -1

    def size(self):
        return self.count
    
    def isEmpty(self):
        return self.count == 0

    def isFull(self):               
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue Full')
        self.rear  = (self.rear + 1) % self.maxCount
        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        self.front = (self.front + 1) % self.maxCount
        x = self.data[self.front]
        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount]