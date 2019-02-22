import heapq
import sys

while True:
    size = int(sys.stdin.readline())
    if size == 0:
        break
    values = list(map(int, sys.stdin.readline().split()))
    cost = 0
    heapq.heapify(values)
    while len(values) > 1:
        pair_cost = heapq.heappop(values) + heapq.heappop(values)
        cost += pair_cost
        heapq.heappush(values, pair_cost)
    print(cost)
