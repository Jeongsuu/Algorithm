# 5355
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    arr = list()
    arr = input().split()
    result = float(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == '@':
            result *= 3
        elif arr[i] == '%':
            result += 5
        elif arr[i] == '#':
            result -= 7
    print("%.2f" %(float(result)))