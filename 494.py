import sys
import re

for line in sys.stdin:
    line = re.findall(r'[A-Za-z]+', line)
    print(len(line))
