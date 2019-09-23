# -*- coding: utf-8 -*- 

# if문

#1330
"""
a,b = input().split()
a = int(a)
b = int(b)
if a>b :
    print(">")
elif a<b :
    print("<")
else:
    print("==")
"""

#9498
"""
score = int(input())

if score >= 90 : print("A")
elif score >=80 : print("B")
elif score >= 70 : print("C")
elif score >= 60 : print("D")
else : print("F")
"""

#2573
"""
year = int(input())

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("1")
else:
    print("0")
"""

#2884
"""
hour, minute = map(int, input().split())
minute -= 45
if(minute < 0):
    minute += 60
    hour -= 1
    if(hour < 0):
        hour = 23
print("%s %s" %(str(hour), str(minute)))
"""

#10817
"""
x = map(int, input().split())
x = sorted(x)
print(x[1])
"""    