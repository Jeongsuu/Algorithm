#Circular Queues

---

### 큐의 활용

>- 자료를 생성하는 작업과 그 자료를 이용하는 작업이 비동기적으로 일어나는 경우
>- 자료를 생성하는 작업이 여러 곳에서 일어나는 경우
>- 자료를 이용하는 작업이 여러 곳에서 일어나는 경우
>- 자료를 생성하는 작업과 그 자료를 이용하는 작업이 양쪽 다 여러 곳에서 일어나는 경우
>- 자료를 처리하여 새로운 자료를 생성하고 , 나중에 그 자료를 다시 처리해야 하는 작업의 경우



### 환형 큐 (Circular Queue)

- **정해진 개수**의 저장 공간을 원형으로 돌려가며 이용한다.
- 큐가 가득 차면, 더이상 원소를 넣을 수 없기 때문에 큐의 길이를 기억하고 있어야한다. 
- enqueue는 rear pointer , dequeue는 front pointer를 이용한다.
- front와 rear를 적절히 게산하여 일차원 배열을 환형으로 재활용하여 사용하는것이 환형 큐의 핵심이다.



### 환형 큐 의 추상적 자료구조 구현

> #### 연산의 정의
>
>* **size()** - 현재 큐에 들어 있는 데이터 원소의 수를 구한다.
>* **isEmpty()** - 현재 큐가 비어있는지를 판단
>* **isFull()** - 큐에 데이터 원소가 꽉 차 있는지를 판단
>* **enqueue(x)** - 데이터 원소 x를 큐에 추가
>* **dequeue()** - 큐의 맨 앞에 저장된 데이터 원소를 제거하며 반홙
>* **peek()** - 큐의 맨 앞에 저장된 데이터 원소를 반환(제거 X)



### 일차원 배열로 구현한 환형 큐

```python
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
```

