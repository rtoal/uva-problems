import sys
cases = int(sys.stdin.readline())
for _ in range(cases):
    farmers = int(sys.stdin.readline())
    total = 0
    for _ in range(farmers):
        size, _, friendliness = map(int, sys.stdin.readline().split())
        total += size * friendliness
    print(total)
