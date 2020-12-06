
def parse_data():
    with open('input.txt', 'r') as input:
        letters = []
        for line in input.readlines():
            if line == '\n':
                yield set.intersection(*letters)
                letters = []
            else:
                line = line.replace('\n', '')
                letters.append({*line})
        yield set.intersection(*letters)

cpt = 0
for s in parse_data():
    cpt += len(s)
print(cpt)