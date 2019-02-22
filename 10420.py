import sys
from collections import Counter

cases = int(sys.stdin.readline())

conquests = Counter()
for _ in range(cases):
    words = sys.stdin.readline().strip().split()
    conquests[words[0]] += 1

for country, count in sorted(conquests.items()):
    print(country, count)
