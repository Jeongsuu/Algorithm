# Queues

---



>스택과 더불어 매우 빈번히 이용되는 자료구조 큐에 대해 공부해보자.
>
>**큐** 또한 데이터 원소를 한 줄로 늘어세우는 자료구조, 즉 선형 자료구조라는 측면에서는 선형 배열, 연결 리스트, 스택과 마찬가지이지만 다른 특성을 가지고 있다.
>
>**스택**에서는 어느 시점에서 스택에 들어있는 데이터 원소를 꺼낼 경우, 가장 최근에 넣었던 원소, 즉 스택 최상단에 자리잡고 있는 원소가 꺼내진다. 이러한 특징을 우리는 **후입선출 (LIFO)**이라고 앞서 공부한 바 있다.
>
>**큐**에서는 **스택**과는 반대로, 어느 시점에서 **큐**에 들어있는 데이터 원소를 꺼내면 **큐**에 들어있는 원소 중 가장 먼저 넣었던 것이 꺼내진다. 따라서 큐를 **선입선출 (FIFO)**이라고도 부른다.
>
>데이터 원소를 큐에 넣는 동작을 **인큐 (enqueue)**연산이라고 부르며, 반대로 큐로부터 데이터 원소를 꺼내는 동작을 **디큐(dequeue)**연산이라고 부른다. 이 두가지 핵심 연산을 포함한 큐의 추상적 자료구조를 공부해본다.



큐는 한 쪽 끝에서 반대쪽 끝에서 뽑아내기 때문에 선입선출 특징을 가지는 선형 자료구조다.

###**큐의 추상적 자료구조 구현**

(1) 배열을 이용하여 구현

- Python 리스트와 메서드들을 이용

(2) 연결 리스트 (linked list)를 이용하여 구현

* 양방향 연결 리스트 이용

###**연산의 정의**

> **size()** - 현재 큐에 들어 있는 데이터 원소의 수
>
> **isEmpty()** - 현재 큐가 비어 있는지를 판단
>
> **enqueue(x)** - 데이터 원소 x를 큐에 추가
>
> **dequeue()** - 큐의 맨 앞에 저장된 데이터 원소를 제거 또는 반환
>
> **peek()** - 큐의 맨 앞에 저장된 데이터 원소를 반환 (제거하지는 않음)		

```python
# 배열로 구현한 큐

class ArrayQueue:
  
  def __init__(self):					# 빈 큐 초기화, constructor method
    self.data = []
  
  def size(self):							# 큐의 크기 리턴
    return len(self.data)
  
  def isEmpty(self):					# 큐가 비어있는지 판단
    return size(self) == 0
  
  def enqueue(self, item):		# 현재 리스트 맨 끝에 데이터 원소 추가
    self.data.append(item)
    
  def dequeue(self):					# 0번 idx, 즉 제일 앞 원소 삭제 및 반환
    return self.data.pop(0)
  
 	def peek(self):							# 0번 idx, 즉 제일 앞 원소 반환
    return self.data[0]
```



### 배열로 구현한 큐의 연산 복잡도

|   연산    |   복잡도   |
| :-------: | :--------: |
|  size()   |   O(N)   |
| isEmpty() |   O(N)   |
| enqueue() |   O(N)   |
| dequeue() | O(N) |
|  peek()   |   O(N)   |

**dequeue()의 경우, 큐의 길이에 비례하는 복잡도를 갖는다.**

왜냐하면, dequeue() 연산은 배열의 맨 앞 원소를 꺼내야 한다. 

<u>맨앞에 원소를 꺼내서 없앤다면 그 뒤에 있는 원소들을 한칸씩 앞으로 이동해야 하기 때문이다.</u>

![image-20191010004319955](/Users/yeojaeng/Library/Application Support/typora-user-images/image-20191010004319955.png)

Queue 모듈에서 기본적으로 제공하는 메서드들은 위 그림과 같다.

```python
class LinkedListQueue:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.data.size()==0

    def enqueue(self, item):
        node = Node(item)
        self.data.insertAt(self.data.nodeCount+1 ,node)

    def dequeue(self):
        return self.data.popAt(1)

    def peek(self):
        return self.data.getAt(1).data
```

---
---

<br>

<br>

## Collections 모듈의 deque 객체
---

`Python` 에서는 `collections` 모듈의 `deque` 객체를 이용하여 큐를 이용할 수 있다.

`deque`란, 스택과 큐를 합친 자료구조로서 가장자리에 원소를 넣거나 뺄 수 있다.

<br>

### deque - init

deque를 이용해 큐 생성시 사용한다.

```python

from collections import deque

# 빈 큐 생성
queue = deque()

# 원소와 함께 생성
queue = deque([1, 2, 3])

# 최대 길이 지정하여 생성
queue = deque(maxlen = 3)

```


### deque - append(x)

생성한 큐에 원소를 삽입할 때 사용한다.


```python
my_deque = deque()
my_deque.append(3)
print(my_deque)   # deque([3])
```

### deque - popleft()

큐에서 원소를 제거할 때 사용한다.

```python
my_deque = deque([1, 2, 3])

while my_deque:
  print("popleft: {}".format(my_deque.popleft()))

# popleft: 1
# popleft: 2
# popleft: 3
```

### deque - clear()

```python
queue = deque([1, 2, 3])

print(queue)
queue.clear()
print(queue)

# deque([1, 2, 3])
# deque([])

```




