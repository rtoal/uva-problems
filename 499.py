import sys
from collections import Counter
from string import ascii_letters

for line in sys.stdin:
    counts = Counter(c for c in line if c in ascii_letters)
    max_count = counts.most_common(1)[0][1]
    letters = [w for w,c in counts.items() if c == max_count]
    print(''.join(sorted(letters)), max_count)
