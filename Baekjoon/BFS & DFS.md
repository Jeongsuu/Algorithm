# BFS & DFS
---

## BFS (Breath - First - Search)7u7jujjjuuujjjj
---


```python

from collections import deque

# BFS (Breath - First - Search), 너비 우선 탐색 구현

graph = {                   # dictionary
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}

def bfs(graph, start_node):
    visited = list()
    queue = deque()

    queue.append(start_node)        # start

    while queue:
        node = queue.popleft()      # instead of 'node = queue.pop(0)'
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited


print(bfs(graph, 'A'))

# ['A', 'B', 'C', 'H', 'D', 'I', 'J', 'M', 'E', 'G', 'K', 'F', 'L']

```

탐색하고자 하는 대상인 `graph` 를 딕셔너리 형태로 `key` 값에는 노드 , `value` 값은 `key`값과 연결되어 있는 노드들을 `list` 형태로 연결해준다.

BFS, 너비 우선 탐색 방식은 한 단계씩 나아가면서 해당 노드와 같은 레벨에 있는 노드(즉, 형제 노드)들을 먼저 순회하는 방식이다.

<br>
<br>


### 코드 설명
---

```python
visited = []
queue = deque()
```

`visited` 리스트는 방문했던 노드들의 목록을 순차적으로 저장할 리스트며, `queue`는 다음으로 방문해야 할 노드들의 목록을 차례대로 저장하기 위한 변수다.

여기서 `queue` 변수에 `deque` 자료형을 쓴 이유는 추후에 설명하도록 하겠다.

```python
queue.append(start_node)
```

탐색을 시작할 시작 노드를 `queue`에 `append`해준다.

```python
while queue:
    node = queue.popleft()
    if node not in visited:
        visited.append(node)
        queue.extend[graph[node])

return visited
```

이후 `queue`를 전부 순회할 때 까지 (탐색하지 못한 노드가 없을때까지) 반복을 진행한다.

`queue`에 제일 앞에있는 `node`를 `popleft()` 메서드를 통해 `node` 변수로 꺼내온다.

여기서 일반 자료형 `list`를 쓰지 않은 이유가 나온다.

`list` 자료구조를 써서 제일 앞에 있는 노드를 가져오기 위해서는 `pop(0)` 메서드를 사용해야 하는데 이는 시간복잡도가 `O(N)` 으로 매우 비효율적이다. 

제일 앞 원소를 뽑은 뒤 이후에 있는 원소들을 모두 한칸씩 땡겨줘야 하기 때문이다.

따라서, `deque` 자료구조를 이용하여 `popleft()` 메서드를 통해 연산의 효율성을 챙긴다.

`deque` 자료구조에 들어있는 원소중 제일 앞에 있는 노드를 꺼내서 해당 노드가 `visited` 배열에 있는지 확인한다.

없다면 `visited` 배열에 이를 추가해주고 `queue` 자료구조에 앞서 꺼냈던 노드와 관계를 가지고 있는 노드들을 모두 `extend` 해준다.

**정리**
> 1. visited & queue 생성
>
> 2. 시작 노드를 `queue`에 append
>
> 3. while queue:
>
> 4. 큐에 0번째 원소를 꺼내온다.
>
> 5. 해당 노드가 `visited` 배열에 없다면 추가하고 해당 노드의 자식 노드들을 `queue`에 추가해준다.

이와 같이 자식 노드들을 `queue`에 추가해주면서 큐에 먼저 추가해줬던 노드들을 우선적으로 방문하게 되면 결국 BFS 형태로 순회하게 된다.

<br>
<br>

## DFS
---

`DFS` 또한 `BFS` 와 비슷하다.

`BFS`에서는 `FIFO(First-In-First-Out)` 성격을 갖는 `queue` 자료구조를 이용했다면 `DFS` 에서는 `FILO(First-In-Last-Out)` 성격을 갖는 `Stack` 자료구조를 이용한다.

```python
def dfs(graph, start_node):         # stack
    visited = list()
    stack = list()

    stack.append(start_node)        # insert the start-node

    while stack:
        node = stack.pop()          
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(graph[node]))

    return visited

# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
```

DFS 는 `queue` 대신 `stack`의 자료구조를 이용한다.

이를 통해 `Depth` 를 우선적으로 탐색할 수 있다.

<br>
<br>

### 코드 설명
---

```python
visited = list()
stack = list()
```

방문한 노드들을 저장할 `visited` 리스트와 아직 방문하지 못한 노드들을 저장할 `stack` 리스트를 생성한다.

```python
stack.append(start_node)
```

방문을 시작할 시작점 노드를 `stack` 에 `push` 해준다.

```python
while stack:
    node = stack.pop()
    if node not in visited:
        visited.append(node)
        stack.extend(reversed(graph[node])))

return visited
```

`stack`의 최상단 노드를 `pop` 하여 `node` 변수에 넣어준다.

해당 노드를 방문하지 않았다면, `visited` 배열에 이를 추가하고 노드의 자식노드들을 `reversed` 하여 `extend`해준다.

여기서 `reversed` 를 진행해주지 않으면 `stack`에 자식노드들을 `push` 해줄 떄 그래프상 왼쪽 노드들부터 들어가기 때문에 오른쪽 노드들이 우선적으로 `pop` 된다.

그렇게 되면 전체 그래프에서 오른쪽 방향부터 깊이 우선 탐색을 진행하게 된다.

왼쪽 방향부터 깊이 우선 탐색을 진행하기 위해 `stack` 배열에 `extend` 시에는 `reversed` 하여 값을 `push`한다.

이 과정을 반복하면 깊이 우선 탐색이 진행된다.

