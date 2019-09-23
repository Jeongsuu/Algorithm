# -*- coding: utf-8 -*- 
#2751
#수 정렬하기 2
# N개의 수가 주어졌을떄, 이를 오름차순으로 정렬하는 프로그램 작성
# 입력 : 첫째줄 N개, 둘째 줄부터 N개의 줄에는 숫자가 주어진다.
# 출력 : N개의 줄에 오름차순 정렬 결과

n = int(input())
numList = []
#입력
for i in range(n):
    numList.append(int(input()))
numList.sort()  # 오름차순 정렬
#출력
for i in range(n):
    print(numList[i])