import sys

num_cases = int(sys.stdin.readline())
for case in range(1, num_cases + 1):
    stops = int(sys.stdin.readline())
    maybe_start = 1
    start, end = 999999, 0
    total, best_so_far = 0, 0
    for maybe_end in range(2, stops + 1):
        total += int(sys.stdin.readline())
        if total < 0: total, maybe_start = 0, maybe_end
        if total >= best_so_far:
            if total > best_so_far or maybe_end - maybe_start > end - start:
                start, end = maybe_start, maybe_end
            best_so_far = total
    if best_so_far > 0:
        print("The nicest part of route {} is between stops {} and {}".format(case, start, end))
    else:
        print("Route {} has no nice parts".format(case))
