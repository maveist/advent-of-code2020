def generate_map():
    lines = []
    with open("input.txt", "r") as input:
        for line in input.readlines():
            lines.append(line.replace("\n", ""))
    return lines


def count_tree(right, down, maps):
    tree_encoutered = 0
    for i in range(0, len(maps), down):
        if maps[i][i//down * right % 31] == "#": # 31 -> len of one line
            tree_encoutered += 1
    return tree_encoutered


maps = generate_map()
res = 1
for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    print(count_tree(right, down, maps))
    res *= count_tree(right, down, maps)
print(res)
