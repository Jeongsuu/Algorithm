from sys import stdin

S = list(stdin.readline().strip())

arr = []

for i in range(len(S)):
    arr.append(S[i:])

for i in range(len(arr)):
    arr[i] = ''.join(arr[i])

arr = sorted(arr)

for i in arr:
    print(i)


