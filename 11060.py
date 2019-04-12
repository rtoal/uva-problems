import sys
from collections import OrderedDict

case = 0
while True:
    line = sys.stdin.readline()
    if not line: break
    if not line.strip(): continue
    nodes = int(line)
    g = OrderedDict()
    for n in range(nodes):
        drink = sys.stdin.readline().strip()
        g[drink] = [0, []]
    edges = int(sys.stdin.readline())
    for e in range(edges):
        d1, d2 = sys.stdin.readline().split()
        g[d1][1].append(d2)
        g[d2][0] += 1
    results = []
    while g:
        for d, neighbors in list(g.items()):
            preds, succs = neighbors
            if preds == 0:
                for drink in succs:
                    g[drink][0] -= 1
                results.append(d)
                g.pop(d)
                break
    case += 1
    print('Case #{}: Dilbert should drink beverages in this order: {}'.format(
        case, ' '.join(results)), end='.\n\n')
