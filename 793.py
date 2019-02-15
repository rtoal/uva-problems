import sys

class DisjointSet():
    def __init__(self):
        self.network = {}
    def add(self, x):
        if x not in self.network:
            self.network[x] = [x, None, 1]
    def union(self, x, y): # return the size of the new group
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return x_root[2]
        if x_root[2] < y_root[2]:
            x_root, y_root = y_root, x_root
        y_root[1] = x_root[0]
        x_root[2] += y_root[2]
        return x_root[2]
    def find(self, x):
        if self.network[x][1] is not None:
            self.network[x] = self.find(self.network[x][1])
        return self.network[x]

cases = int(sys.stdin.readline())
blank = sys.stdin.readline()
for case in range(cases):
    if case != 0:
        print()
    network = DisjointSet()
    computers = int(sys.stdin.readline())
    for c in range(1, computers+1):
        network.add(c)
    found, not_found = 0, 0
    while True:
        try:
            letter, x, y = sys.stdin.readline().split()
            x = int(x)
            y = int(y)
            if letter == 'c':
                network.union(x, y)
            elif letter == 'q':
                x_root = network.find(x)
                y_root = network.find(y)
                if x_root == y_root:
                    found += 1
                else:
                    not_found += 1
        except:
            break

    print("{},{}".format(found, not_found))
