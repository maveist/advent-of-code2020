NUMBER_ROWS = 127
NUMBER_COLS = 8


def parse_data():
    list_seat = []
    with open('input.txt', 'r') as input:
        for line in input.readlines():
            list_seat.append(line.replace('\n', ''))
    return list_seat


def get_seat(line):
    row_min, col_min, row_max, col_max = (0,0,NUMBER_ROWS, NUMBER_COLS)
    for char in line:
        if char == 'B':
            row_min = (row_max + row_min) // 2
        if char == 'F':
            row_max = (row_max+row_min) // 2
        if char == 'R':
            col_min = (col_max+col_min) // 2
        if char == 'L':
            col_max = (col_max+col_min) // 2
    return row_max * 8 + col_min

# part 1
seats = []
for line in parse_data():
    seats.append(get_seat(line))
print("highest seat:", max(seats))

# part 2
seats.sort()
for i in range(seats[0], len(seats)):
    if i not in seats:
        print("missing seat:", i)
        break