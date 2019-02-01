import sys
cases = int(sys.stdin.readline())
for _ in range(cases):
    x, y = map(int, sys.stdin.readline().split())
    if x < y:
        print('<')
    elif x > y:
        print('>')
    else:
        print('=')
