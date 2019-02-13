import sys

# Nodes are triples [data, parent, size]

def add(whole, data):
    if data not in whole:
        whole[data] = [data, data, 1]

def find(whole, data):
    if data != whole[data][1]:
        whole[data] = find(whole, whole[data][1])
    return whole[data]

def union(whole, x, y):
    x_root = find(whole, x)
    y_root = find(whole, y)
    if x_root == y_root:
        return x_root[2]
    if x_root[2] < y_root[2]:
        x_root, y_root = y_root, x_root
    y_root[1] = x_root[0]
    x_root[2] += y_root[2]
    return x_root[2]

cases = int(sys.stdin.readline())
for _ in range(cases):
   num_connections = int(sys.stdin.readline())
   whole = {}
   for connections in range(num_connections):
       friends = sys.stdin.readline().strip().split()
       add(whole, friends[0])
       add(whole, friends[1])
       print(union(whole, friends[0], friends[1]))
