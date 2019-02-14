import sys

field_number = 1
while True:
    rows, cols = map(int, sys.stdin.readline().split())
    if (rows, cols) == (0, 0):
        break
    elif field_number != 1:
        print()
    print('Field #{}:'.format(field_number))
    field_number += 1

    # Read in ENTIRE field
    field = [[0]*cols for _ in range(rows)]
    for row in range(rows):
        line = sys.stdin.readline().strip()
        field[row] = list(line)

    for row in range(rows):
        for col in range(cols):
            cell = field[row][col]
            count = 0
            if cell != '*':
                if row-1>=0 and col-1>=0 and field[row-1][col-1]=='*': count += 1
                if row-1>=0 and field[row-1][col]=='*': count += 1
                if row-1>=0 and col+1<cols and field[row-1][col+1]=='*': count += 1
                if col-1>=0 and field[row][col-1]=='*': count += 1
                if col+1<cols and field[row][col+1]=='*': count += 1
                if row+1<rows and col-1>=0 and field[row+1][col-1]=='*': count += 1
                if row+1<rows and field[row+1][col]=='*': count += 1
                if row+1<rows and col+1<cols and field[row+1][col+1]=='*': count += 1
                field[row][col] = count
        print(''.join(str(cell) for cell in field[row]))
