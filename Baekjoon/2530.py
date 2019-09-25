#2525 오븐시계
import sys

def sol(total):
    h = total // 3600
    total %= 3600
    m = total // 60
    total %= 60
    s = total
    print("%d %d %d" %(h,m,s)) 

a, b, c = map(int, sys.stdin.readline().split())
d = int(sys.stdin.readline())
total = (a*3600) + (b*60) + c + d
h=0
m=0
s=0
if total >= 86400:
    total %= 86400
    sol(total)
    # h = total // 3600
    # total %= 3600
    # m = total // 60
    # total %= 60
    # s = total
else:
    sol(total)
#     h = total // 3600
#     total %= 3600
#     m = total // 60
#     total %= 60
#     s = total
# print("%d %d %d"%(h, m, s))