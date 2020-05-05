from sys import stdin

while True:
    arr = list(stdin.readline())
    lower_cnt, upper_cnt, num_cnt, space_cnt = 0
    if not arr:
        break
    for i in range(len(arr)):
        if arr[i].isupper():
            upper_cnt += 1
        elif arr[i].islower():
            lower_cnt += 1
        elif arr[i] == ' ':
            space_cnt += 1
        elif arr[i].isdigit():
            num_cnt += 1
    print("{} {} {} {}".format(lower_cnt, upper_cnt, num_cnt, space_cnt))
