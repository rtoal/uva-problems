import sys
import math

while True:
    try:
        x, y, z = map(float, sys.stdin.readline().split())
        if x <= 0 or y <= 0 or z <= 0:
            radius = 0
        else:
            hp = (x + y + z) / 2
            a = math.sqrt(hp * (hp-x) * (hp-y) * (hp-z))
            p = x + y + z
            radius = (2 * a) / p
        print('The radius of the round table is: {:.3f}'.format(radius))
    except:
        break
