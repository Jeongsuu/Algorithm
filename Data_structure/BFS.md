# BFS (Breath First Search)

---



### 1. 개념

---

>* 파이썬 BFS 구현
>
>* 큐를 사용하여 구현
>
>* 아래와 같은 그래프 예시를 통한 BFS 시뮬레이션
>
>  <img width="279" alt="스크린샷 2019-10-21 오후 2 44 50" src="https://user-images.githubusercontent.com/33051018/67179478-5e95ae80-f411-11e9-8ffd-4df55af16b0c.png">
>
>  | **출력** | **기존 입력** | **새로운 입력 ( 자손 )** |
>  | -------- | ------------- | ------------------------ |
>  |          |               | **A**                    |
>  | **A**    |               | **B C D**                |
>  | **B**    | **C D**       | **E F**                  |
>  | **C**    | **D E F**     | **G**                    |
>  | **D**    | **E F G**     | **H I**                  |
>  | **E**    | **F G H I**   |                          |
>  | **F**    | **G H I**     | **J**                    |
>  | **G**    | **H I J**     |                          |
>  | **H**    | **I J**       |                          |
>  | **I**    | **J**         | **K L**                  |
>  | **J**    | **K L**       |                          |
>  | **K**    | **L**         |                          |
>  | **L**    |               |                          |
>
>
>  탐색 결과 : **A -> B -> C -> D -> E -> F -> G -> H -> I -> J -> K -> L** 



### 2. 구현

---

>```python
>graph = { 
>        'A' : set(['B', 'C', 'D']),
>        'B' : set(['A', 'E', 'F']),
>        'C' : set(['A', 'G']),
>        'D' : set(['A', 'H', 'I']),
>        'E' : set(['B']),
>        'F' : set(['B', 'J']),
>        'G' : set(['C']),
>        'H' : set(['D']),
>        'I' : set(['D', 'K', 'L']),
>        'J' : set(['F']),
>        'K' : set(['I']),
>        'L' : set(['I'])
>        }
># 해당 노드에 연결된 노드들의 set을 대응시킨 dict 자료형으로 그래프 표현
>
>def BFS(graph, start):
>    queue = [start]
>    visited = []									# 방문 기록 배열
>    
>    while queue:									# 큐가 빌 때 까지 반복
>        curr_node = queue.pop(0)					# 큐의 0번째 원소 pop
>        if curr_node not in visited:				# 방문하지 않았다면		
>            visited.append(curr_node)				# 방문 배열에 추가
>            queue += graph[curr_node] - set(visited)# 해당 노드의 자식노드중 방문하지 않은 노드를 queue에 추가
>    return visited
>
>print(BFS(graph, 'A'))
>
># ['A', 'B', 'D', 'C', 'E', 'F', 'H', 'I', 'G', 'J', 'K', 'L']
>```
>
>BFS 알고리즘 또한 마찬가지로 그래프에서 모든 `vertex`를 탐색하기 위한 `완전탐색 알고리즘`이다.
>
>위 예시를 보다시피, BFS(graph, 'A")의 결과값이 우리가 예상했던 BFS 의 결과와는 약간의 차이가 존재한다.
>
>**이것 또한 DFS때와 마찬가지로 `visited list`는 `unordered`한 자료형이기 때문이다.**
>
>**중요한 것은 BFS 알고리즘을 통해 그래프 내 모든 `vertex`를 탐색했느냐 **이다

