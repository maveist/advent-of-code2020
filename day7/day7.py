import re

pattern = re.compile(r"([0-9] )*([a-zA-Z]+ [a-zA-Z]+) (bags|bag)")
searched_color = "shiny gold"

def parse_data():
    rules = {}
    with open("input.txt", "r") as input:
        for line in input.readlines():
            res = pattern.findall(line)
            container = res[0][1]
            rule = {}
            if "no other bags" not in line:
                for i in range(1, len(res)):
                    rule[res[i][1]] = int(res[i][0])
            rules[container] = rule
    return rules

class Checker:

    def __init__(self, rules):
        self.checked = []
        self.can_contain = set()
        self.rules = rules
        self.counter = {}

    def check(self, color):
        if color not in self.checked:
            self.checked.append(color)
            if searched_color in rules[color].keys():
                self.can_contain.add(color)
                return True
            else:
                res = max([False]+[self.check(clr) for clr in rules[color].keys()])
                if res:
                    self.can_contain.add(color)
                return res
        else:
            return color in self.can_contain

    def count(self, color):
        if color not in self.counter.keys():
            count = 1 + sum([self.rules[color][clr] * self.count(clr) for clr in self.rules[color]])
            self.counter[color] = count
            return count
        else:
            return self.counter[color]

# part 1
rules = parse_data()
checker = Checker(rules)
for color in rules.keys():
    checker.check(color)
# part 2
print(len(checker.can_contain))
print(checker.count("shiny gold") - 1)