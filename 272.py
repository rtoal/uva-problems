import sys

open = True
for c in sys.stdin.read():
    if (c == '"'):
        print("``" if open else "''", end='')
        open = not open
    else:
        print(c, end='')
