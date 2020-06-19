## Linked Lists

<hr/>
### 기본적 연결 리스트

- **Node : Data + Link (next)**
- **노드 내의 데이터는 다른 구조로 이루어질 수 있음 ex)문자열, 레코드, 또 다른 연결리스트…etc**
- **리스트의 맨 첫 원소 : Head, 맨 끝 원소 : Tail, 노드의 개수 매우 중요!**



### 자료구조 정의

* **Node : Data + Link(next)**
* **LinkedList**

```python
class Node:
  def __init__(self, item):
    self.data = item
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.nodeCount = 0
    self.head = None
    self.tail = None
    
```



### 연산 정의

>1. 특정 원소 참조 (k번째)
>2. 리스트 순회
>3. 길이 얻어내기
>4. 원소 삽입
>5. 원소 삭제
>6. 두 리스트 병합

**1. 특정 원소 참조**

```python
def getAt(self, pos):
        # 원소 위치 입력이 잘못된 경우
        if pos <= 0 or pos > self.nodeCount:
            return None
        idx = 1
        currentNode = self.head # 현재 노드를 head 노드로 초기화
        print(type(currentNode))
        while i < pos:
            currentNode = currentNode.next
            idx += 1
        return currentNode
      
```



**2. 리스트 순회**

```python
def traverse(self):
  traverse_result = list()
  currentNode = self.head				# 현재 노드를 head 노드로 초기화
  while currentNode:						# 노드를 모두 순회할 때 까지 반복
    traverse_result.append(currentNode.data)		# 현재 노드의 데이터값을 순회결과 리스트에 append
    currentNode = currentNode.next							# 다음 노드로 넘어가도록 링크
  
  return traverse_result

```



**3.길이 얻어내기**

```python
def getLength(self):
  return self.nodeCount
```



**4. 원소 삽입**

>```python
>def insertAt(self, pos, newNode):
>```
>
>- pos가 가리키는 위치는 1 <= pos <= nodeCount+1 내에 존재한다.
>  - pos == nodeCount+1 인 경우, tail 뒤에 삽입하기 위한 위치선정.
>- newNode를 삽입하고 성공/실패에 따라 return True/False
>
>**Operate Specification**
>
>1. **prev.next가 가리키고 있던 pos 노드를 newNode.next가 가리키도록 한다.**
>2. **prev.next가 newNode를 가리키도록 한다.**
>3. **nodeCount += 1**
>
>위 내용을 코드화 해본다.

```python
def insertAt(self, pos, newNode):
  prev = self.getAt(pos - 1)		# 삽입하고자 하는 위치 이전에 위치하는 노드를 prev에 저장한다.
  newNode.next = prev.next			# prev의 link가 가리키고 있는 노드를 새로운 노드의 link가 가리키도록 한다.
  prev.next = newNode						# 이전 노드의 link가 새로운 노드를 가리키도록 한다.
  self.nodeCount += 1						# nodeCount값을 1 올린다.
```

>**코드 구현시 주의해야 할 사항**
>
>* 삽입하려는 위치가 리스트의 맨 앞인 경우
>  * prev가 없다.
>  * Head 조정 필요
>
>* 삽입하려는 위치가 리스트 맨 끝인 경우
>  * Tail 조정 필요
>
>* 빈 리스트에 삽입하는 경우
>  * 위 두 조건에 의해 처리된다
>
>주의 사항을 반영하여 코드를 재작성한다.
>
>```python
>def insertAt(self, pos, newNode):
>        if pos < 1 or pos > self.nodeCount + 1: # pos가 올바른 값을 가지는 범위에 있는지 확인
>            return False    
>        
>        if pos == 1:                   # 리스트 맨 앞에 삽입하는 경우
>            newNode.next = self.head
>            self.head = newNode
>        else:                          
>            if pos == self.nodeCount + 1:   #리스트 맨 뒤에 삽입하는 경우
>                prev = self.tail
>            else:
>                prev = self.getAt(pos - 1)
>            newNode.next = prev.next
>            prev.next = newNode
>        
>        if pos == self.nodeCount + 1:
>            self.tail = newNode
>            
>        self.nodeCount += 1
>        return True
>     
>```



### 연결 리스트 원소 삽입의 복잡도

- 맨 앞에 삽입하는 경우 : O(1)  
- 중간에 삽입하는 경우 :  O(n)
- 맨 끝에 삽입하는 경우 : O(1)         # tail pointer를 가지고 있기 때문에 상수시간 복잡도를 갖는다. 



**5. 원소 삭제**

>```python
>def popAt(self, pos):
>```
>
>- pos가 가리키는 위치는 1 <= pos <= nodeCount 사이에 존재한다.
>- node 삭제 후 그 node를 return 한다.
>
>**Operation Specification**
>
>1. **urrentNode.next가 가리키고 있는 노드를 prev.next가 가리키도록 한다.**
>2. **currentNode.data를 return 한다**
>3. **nodeCount -= 1**
>
>**코드 구현 주의사항**
>
>* 삭제하려는 node가 맨 앞에 위치하고 있는 node 인 경우
>  * prev가 없음
>  * Head 조정 필요
>
>* 삭제하려는 node가 리스트 맨 끝의 node인 경우
>  * Tail 조정 필요



### 연결 리스트 원소 삭제 복잡도

* 맨 앞에서 삭제하는 경우 : O(1)
* 중간에서 삭제하는 경우 : O(n)
* 맨 끝에서 삭제하는 경우 : O(n)



**6. 리스트 병합**

>```python
>def concat(self, L):
>  self.tail.next = L.head
>  if L.tail:
>		   self.tail = L.tail
>  self.nodeCount += L.nodeCount	
>```















 