import itertools

input_list = []

with open("input.txt", "r") as input:
    input_list = [int(line) for line in input.readlines()]


for a, b, c in itertools.product(input_list, input_list, input_list):
    if a + b + c == 2020:
        print(a*b*c)
        break