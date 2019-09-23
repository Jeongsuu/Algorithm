# -*- coding: utf-8 -*- 

# for문

#2739
"""
n = int(input())

for i in range(1, 10) :
    print("{0} * {1} = {2}".format(n, i, n*i))
"""

#10950
"""
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a+b)
"""

#8393
"""
n = int(input())
result = 0
for i in range (1, n+1):
    result += i
print(result)
"""

#15552
"""
import sys
t = int(sys.stdin.readline().rstrip())
for i in range (t):
    a,b = map(int, sys.stdin.readline().split())
    print(a+b)
"""

#2741
"""
import sys
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    print(i+1)
"""

#2742
"""
n = int(input())
for i in range(n, 0, -1):   #n 부터 0까지 -1
    print(i)
"""

#11021
"""
import sys
t = int(sys.stdin.readline().rstrip())
for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1}".format(i+1, a+b))
"""

#11022
"""
import sys
t = int(sys.stdin.readline().rstrip())
for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    print("Case #{0}: {1} + {2} = {3}".format(i+1, a, b, a+b))
"""

#2438
"""
import sys
t = int(sys.stdin.readline())

for i in range(t):
    for j in range(i+1):
         print("*" ,end = '')
    print()
"""

#2439 
""" 
import sys
n = int(sys.stdin.readline())
for i in range(1, n+1):
    print(" "*(n-i) + "*"*i)
"""

#10871
'''
n,x = map(int, input().split())
l = list(map(int, input().split()))

for i in range(n):
    if x > l[i]:
        print(l[i], end=' ')
'''
