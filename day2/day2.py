import re

pattern = re.compile(r"([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)")
list_criteria = []
with open("input.txt", "r") as input:
    for line in input.readlines():
        res = pattern.match(line)

        list_criteria.append({
            "min": int(res.group(1)),
            "max": int(res.group(2)),
            "letter": res.group(3),
            "phrase": res.group(4)
        })

cpt_good_pwd = 0
# part 1
for passwd in list_criteria:
    occ_letter = len(passwd["phrase"].split(passwd["letter"])) - 1
    if occ_letter >= passwd['min'] and occ_letter <= passwd['max']:
        cpt_good_pwd +=1

# part 2
cpt_good_pwd = 0
for passwd in list_criteria:
    if (passwd["phrase"][passwd["min"] - 1 ] == passwd["letter"]) != ((passwd["phrase"][passwd["max"] - 1 ] == passwd["letter"])):
        cpt_good_pwd +=1
print(cpt_good_pwd)