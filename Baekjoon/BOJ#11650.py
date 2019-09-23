#11650

# 2차원 평면 위 점 N개 , 좌표를 x좌표가 증가하는 순 , x좌표가 같으면 y좌표가 증가하는 순서로 정렬

n = int(input())        #점 개수

crd_list = []   #좌표 리스트
for _ in range(n):
    crd_list.append(list(map(int, input().split())))
    
crd_list.sort()

for crd in crd_list:
    print(*crd)