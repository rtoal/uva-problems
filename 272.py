import sys

replacement = '``'

for line in sys.stdin:
    line = line.strip()
    while True:
        check = line.replace('"', replacement, 1)
        if check == line:
            break
        line = check
        replacement = "''" if replacement == '``' else '``'
    print(line)
