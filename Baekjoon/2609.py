from sys import stdin

a, b = map(int, stdin.readline().split())
gcd = 0
lcm = 0

# gcd
for i in range(1, min(a,b)+1):
    if (a % i) == 0 and (b % i) == 0:
        gcd = i

# lcm
lcm = int(gcd * (a/gcd) * (b/gcd))

print(str(gcd)+'\n'+str(lcm))