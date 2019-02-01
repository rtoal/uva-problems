import sys
cases = int(sys.stdin.readline())
for _ in range(cases):
    n = int(sys.stdin.readline())
    n *= 567
    n //= 9
    n += 7492
    n *= 235
    n //= 47
    n -= 498
    n = abs(n)
    n //= 10
    n %= 10
    print(n)
