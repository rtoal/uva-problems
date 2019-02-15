import sys
import re

for line in sys.stdin:
    print(len(re.findall(r'[A-Za-z]+', line)))
