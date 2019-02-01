import sys

line = sys.stdin.readline()
while line.strip() != '':
    people, budget, hotels, _ = map(int, line.split())
    costs = []
    for _ in range(hotels):
        price = int(sys.stdin.readline())
        max_beds = max(map(int, sys.stdin.readline().split()))
        if max_beds >= people:
            costs.append(price * people)
    if not costs or min(costs) > budget:
        print('stay home')
    else:
        print(min(costs))
    line = sys.stdin.readline()
