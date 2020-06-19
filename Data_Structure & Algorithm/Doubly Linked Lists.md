### 양뱡향 연결  리스트 (Doubly Linked Lists)

---

#### 

#### 양방향 연결 리스트 (Doubly Linked Lists)

- 한 쪽으로만 링크를 연결하지 않고, 양쪽으로 링크를 연결한다.

  - 앞으로도 (다음 Node), 뒤로도 이전 Node) 진행 가능

- 장점

  - 데이터 원소 순회시, 앞에서부터 뒤로도 할 수 있으며 뒤에서부터 앞으로도 가능하다.
    - 실제로 리스트를 대상으로 앞/뒤로 왔다 갔다 하며 작업를 행하는 일들이 빈번히 요구된다.

- 단점

  - 메모리 사용량이 늘어난다.
  - 원소 삽입/삭제 연산에 있어서 앞/뒤 링크를 모두 조정해 주어야한다.

  

- **Node 구조의 확장**

  - ```python
    class Node:
        def __init__(self, item):
            self.data = item
            self.next = None
    ```

  - 기존 코드(위) 를 아래와 같이 확장한다.

    ```python
    class Node:
        def __init__(self, item):
            self.data = item
            self.prev = None
            self.next = None
    ```

- 리스트 처음과 끝에 dummy node를 둔다.

  - 처음과 끝에 dummy node를 넣음으로써 데이터를 담고있는 노드들이 모두 같은 모양을 갖게 된다.

```python
class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self, item):
        self.nodeCount = 0
        self.head = Node(None)		# Dummy Node
        self.tail = Node(None)		# Dummy Node
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None
```

![1570376670198](C:\Users\duwjd\AppData\Roaming\Typora\typora-user-images\1570376670198.png)

* 위 그림과 같이 더미노드로만 이루어진, 빈 양방향 연결 리스트를 생성한다.



이제는 Linked List에서 이용되어지는 연산에 대해서 살펴본다.

1)	**리스트 순회**

```python
def traverse(self):		# 정방향 순회
    result = []
    curr = self.head
    while curr.next.next:		# tail도 Dummy Node가 들어있기 때문에 curr.next.next가 유효한 동안 순회
        curr = curr.next
        result.append(curr.data)
    return result

def reverse_traverse(self):		# 역방향 순회
    result = []
    curr = self.tail
    while curr.prev.rev:		# head도 Dummy Node가 들어있기 때문에 curr.prev.prev가 유효한 동안 순회
        curr = curr.prev
        result.append(curr.data)
    return result
    
```

**양방향 연결 리스트기 때문에 역방향으로의 순회 또한 가능해진다.**

* **순회 핵심 로직**
  * 정방향 순회 : 리스트 맨 끝에는 tail노드, 즉 `Dummy Node`가 위치하기 때문에 `curr.next.next`가 존재할 떄 까지 순회한다.
  * 역방향 순회 : 리스트 맨 앞에는 head노드, 즉 `Dummy Node`가 위치하기 때문에 `curr.prev.prev`가 존재할 때 까지 순회한다.



2) **원소 삽입**

1. newNode 의 양쪽 링크를 조정한다.
2. prev, next의 링크를 조정한다.
3. nodeCount를 올려준다.

```python
def insetAfter(self, prev, newNode):
    next = prev.next		# 다음노드 초기화
    newNode.prev = prev		# newNode의 양쪽 링크 조정
    newNode.next = next
    prev.next = newNode		# 이전 노드의 링크 조정
    next.prev = newNode		# 다음 노드의 링크 조정
    self.nodeCount += 1
    return True
```



3) **원소 얻어내기**

```python
def getAt(self, pos):
    if pos < 0 or pos > self.nodeCount:
        return None
    
    if pos > (self.nodeCount // 2):		#만일 pos값이 뒷쪽에 가깝다면
        i = 0
        curr = self.tail
        while i < self.nodeCount - pos + 1:
            curr = curr.prev
            i += 1
    else:
        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
    return curr.data
        
```

