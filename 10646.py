import sys

def card_value(s):
    return int(s[0]) if s[0] in '23456789' else 10

lines = sys.stdin.readlines()
cases = int(lines[0])
all_cards = ' '.join(lines[1:]).split()
for case in range(cases):
    cards = list(reversed(all_cards[case * 52 : (case+1) * 52]))
    saved25 = cards[0:25]
    pile = cards[25:]
    y = 0
    for _ in range(3):
        x = card_value(pile[0])
        y += x
        pile = pile[1 + (10-x):]
    result = saved25 + pile
    answer = result[len(result) - y]
    print('Case {}: {}'.format(case + 1, answer))
