import sys
for case in range(int(sys.stdin.readline())):
    salaries = map(int, sys.stdin.readline().split())
    middle = sorted(salaries)[1]
    print('Case {}: {}'.format(case + 1, middle))
