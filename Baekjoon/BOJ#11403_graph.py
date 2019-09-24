# 방향그래프 G , 모든정점 (i,j)에 대하여 i에서 j로 가는 경로가 있는지 없는지 구하라.

# input : N, N개의 인접행렬

# output : N개의 줄에 걸쳐 인접행렬 형식으로 출력


n = int(input())
graph=[ [0 for col in range(n)] for row in range(n) ]
for col in range(n):
    for row,val in enumerate(map(int, input().split())):
        graph[col][row] = val
for col in range(n):
    for row in range(n):
        for diag in range(n):
            if graph[row][col] and graph[col][diag]:
                graph[row][diag] = 1
for i in range(n):
    _str = ''
    for j in range(n):
        _str += str(graph[i][j]) + " "
    print(_str)    
                        