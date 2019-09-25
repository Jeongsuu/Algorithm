#2525 오븐시계
import sys
a,b = map(int, sys.stdin.readline().split())
c = int(sys.stdin.readline())
total = a*60 + b + c
if total>= 60*24:
    total %= 1440
print('%d %d' %(total//60, total%60))