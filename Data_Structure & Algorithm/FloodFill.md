# FloodFill Algorithm

<br>

`Flood Fill` 알고리즘은 `DFS(Depth First Search)`에 기반을 두고 응용된 알고리즘이다.

이는 다차원 배열에서 화면을 격자로 분할하거나 채우는 과정에서 사용되는 알고리즘이다.

`Flood Fill` 을 이해하기 위해서는 그래프의 기본적 이해와 연결요소(component)에 관한 개념이 필요하다.

연결요소란, 그래프에서 한번에 연결된 요소들을 의미한다.

![image](https://user-images.githubusercontent.com/33051018/85096122-51de8a00-b22e-11ea-9939-c5915140d74e.png)

위 예시 그래프의 경우에는 3개의 연결요소를 갖는다.

플러드필은 모든 정점에서 DFS 완전탐색을 통해 연결요소가 몇개인지 파악하는 알고리즘이다.

즉, DFS를 탐색한 회수가 곧 연결요소의 개수가 되는 셈이다.

<br>

그렇다면 Flood Fill 알고리즘의 근간이되는 DFS, 깊이 우선 탐색에 대하여 간단히 구현 해보도록 하자.

DFS는 스택 자료구조를 이용해 탐색 노드에 연결된 자식노드를 우선으로 탐색하는 방법이다.

```python

def DFS(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited
```

`Depth`를 우선으로 탐색하기 위해 `graph[node]` 값을 모두 stack에 더하여 맨 뒤의 값부터 pop을 통해 방문을 진행한다.




