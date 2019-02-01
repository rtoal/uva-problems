import sys

print('Lumberjacks:')
cases = int(sys.stdin.readline())
for _ in range(cases):
    a = list(map(int, sys.stdin.readline().split()))
    if all(a[i]<=a[i+1] for i in range(len(a)-1)) or all(a[i]>=a[i+1] for i in range(len(a)-1)):
        print('Ordered')
    else:
        print('Unordered')
