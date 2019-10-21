# DFS (Depth Frist Search) 

---





### 1. 개념

---

>* 파이썬 DFS 구현
>
>* 스택을 사용하여 구현
>
>* 아래와 같은 그래프 예시를 통한 DFS 시뮬레이션
>
>  
>
>  <img width="250" alt="스크린샷 2019-10-21 오후 2 44 50" src="https://user-images.githubusercontent.com/33051018/67179478-5e95ae80-f411-11e9-8ffd-4df55af16b0c.png">
>
>  | 출력  | 기존 입력   | 새로운 입력 ( 자손 ) |
>  | ----- | ----------- | -------------------- |
>  |       |             | **A**                |
>  | **A** |             | **B C D**            |
>  | **D** | **B C**     | **H I**              |
>  | **I** | **B C H**   | **K L**              |
>  | **L** | **B C H K** |                      |
>  | **K** | **B C H**   |                      |
>  | **H** | **B C**     |                      |
>  | **C** | **B**       | **G**                |
>  | **G** | **B**       |                      |
>  | **B** |             | **E F**              |
>  | **F** | **E**       | **J**                |
>  | **J** | **E**       |                      |
>  | **E** |             |                      |
>
>
>  탐색 결과 : **A -> D -> I -> L -> K -> H -> C -> G -> B -> F -> J -> E**

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
>def DFS(graph, start):
>    stack = [start]
>    visited = []  								# 방문 기록 배열
>    
>    while stack:								# 스택이 빌 때 까지 반복
>        curr_node = stack.pop()					# 스택 최상위 원소 pop
>        if curr_node not in visited:			# 방문하지 않았다면
>            visited.append(curr_node)			# 방문 배열에 추가
>            stack += graph[curr_node] - set(visited)	# 해당 노드의 자식노드들 중 방문하지 않은 노드들 stack에 추가
>    return visited
>
>printf(DFS(graph, 'A'))
>
>#['A', 'D', 'I', 'K', 'L', 'H', 'C', 'G', 'B', 'E', 'F', 'J']
>```
>
>참고로 DFS 알고리즘은 그래프에서 모든 `vertex`를 찾아가는 과정이라고 생각하자.
>
>위 예시를 보다시피, DFS(graph, 'A')의 결과값이 우리가 예상했던 순서의 결과와는 다소 차이가 존재한다.
>
>**그 이유는 `visited list`는 `unordered` 하기 때문이다. 즉 순서가 없는 `list` 자료형이기 때문에..**
>
>**중요한 것은 DFS를 통하여 모든 vertex를 탐색했느냐** 이다.
>
>
>
>
>