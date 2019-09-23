# -*- coding: utf-8 -*-

# 1차원 배열

#10818
"""
n = int(input())        #정수형 변수 입력
arr = list(map(int, input().split())) # 정수형 배열 입력받아서 공백기준 split
print(min(arr), max(arr))
"""


#2562
"""
arr = []                # 리스트 생성
for i in range(0, 9):   # 9번 반복
    arr.append(int(input()))    #입력받은 수를 리스트에 append
max = max(arr)
print(max)
print(arr.index(max) + 1)       # 최대값의 인덱스 출력.
"""

#2920
"""
arr = list(map(int, input().split()))

if arr == [1, 2, 3, 4, 5, 6, 7, 8]:
    print("ascending")
elif arr == [8, 7, 6, 5, 4, 3, 2, 1]:
    print("descending")
else:
    print("mixed")
"""

#2577
"""
# A,B,C의 값 받기
A = input()
B = input()
C = input()
# A*B*C의 값 구하기
num = int(A) * int(B) * int(C)
# 결과값을 문자열 배열로 만들기
num = str(num)
# count()써서 개수 구하기
for i in range(0, 10):
     print(num.count(str(i)))
 # count() : 지정된 요소의 리스트 내 개수 반환
"""

#3052
"""
num_list = []        # 입력받은 숫자를 저장할 빈 리스트 생성
rem_list = []        # 나머지값을 저장할 빈 리스트 생성
for _ in range(10):     #10번 반복하겠다
    num_list.append(int(input()))   # 입력받는 숫자를 num_list 배열에 append
for num in num_list:    #num_list 순회
    rem = num % 42      # num값을 42로 나눈 나머지값을 rem 변수에 저장
    if rem in rem_list: # rem_list 배열에 이미 존재하는 값이라면 pass
        pass
    else:               # rem_list 배열에 존재하지 않는 값이라면 
        rem_list.append(rem)    
print(len(rem_list))
"""

#1546
"""
n = int(input()) # 시험 과목 수
score_list = list(map(int, input().split()))    # 점수 입력받을 정수형 배열
m = max(score_list)     # 최대값
total = 0
for i in range(len(score_list)):    # list 순회
    score_list[i] = score_list[i]/m*100 # 새로운 score 계산
    total += score_list[i]      #총합 구하기
print(float(total/len(score_list)))     # 총합 / 과목수 -> 평균
"""

#8958
'''
n = int(input())        # test case 개수
for i in range(n):
    arr = input()       # 배열 입력받기
    total = 0
    score = 0
    for j in range(len(arr)):   배열 순회
        if arr[j] == 'O':   #현재 원소가 O인경우
            score += 1
            total += score
        elif arr[j] == 'X': #현재 원소가 X인경우
            score = 0
    print(total)
'''            

#4344
for i in range(int(input())):           # test case 수 입력받고 해당 수만큼 반복
    list_input = list(map(int, input().split(' ')))         # 입력받은 값을 배열에 저장
    avg = sum(list_input[1:]) / list_input[0]       # 평균 구하기
    cnt = 0
    for j in list_input[1:]:            # 점수값들을 순회하며 평균을 넘는지 확인
        if j > avg:                     # 평균을 넘을경우 cnt 증가
            cnt += 1
    print(str('%.3f' % round(cnt / list_input[0] * 100, 3)) + '%')      # 평균을 넘은 학생 수를 총 학생수로 나눈후 소수점 3째자리까지 출력
        
        

    
            