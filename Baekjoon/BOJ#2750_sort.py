# -*- coding: utf-8 -*- 
#2750
# 정렬하기
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하라

# input : 첫째줄에 N , 둘째줄부터 N개의 숫자 , 수는 중복되지 않는다.
# output : 첫째줄부터 N개의 줄을 오름차순으로 정렬한 결과를 한줄에 하나씩 출력

n = int(input())    # test case 개수
numList = []
for i in range(n):
    numList.append(int(input()))
numList.sort()

for i in range(n):
    print(numList[i])



 
    