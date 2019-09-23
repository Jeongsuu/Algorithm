# 11047
# n : 동전 개수 , k : 만들어야 하는 화폐 가치
n, k =map(int, input().split())
result = 0

# 소유중인 동전 입력받기
coin_arr = [int(input()) for _ in range(n)]

# 최적해 구하기
for i in reversed(range(n)):
    result += k // coin_arr[i]
    k %= coin_arr[i]
print(result)