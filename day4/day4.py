import re


def parse_data():
    list_pprt = []
    pattern = re.compile(r"(iyr|hgt|byr|cid|pid|eyr|hcl|ecl):((#|[a-z]|[0-9]*)*)")
    dict_pprt = {}
    with open("input.txt","r") as input:
        for line in input.readlines():
            if line == '\n':
                list_pprt.append(dict_pprt)
                dict_pprt = {}
            res = pattern.findall(line)
            for info in res:
                dict_pprt[info[0]] = info[1]
    list_pprt.append(dict_pprt)
    return list_pprt


class Validator:

    def validate_byr(self, byr):
        try:
            return 1920 <= int(byr) <= 2002
        except:
            return False

    def validate_iyr(self, iyr):
        try:
            return 2010 <= int(iyr) <= 2020
        except:
            return False

    def validate_eyr(self, eyr):
        try:
            return 2020 <= int(eyr) <= 2030
        except:
            return False

    def validate_hgt(self, hgt):
        res = re.match(r"([0-9]*)(cm|in)", hgt)
        if res is not None:
            value = int(res.group(1))
            metric = res.group(2)
            if metric == "in":
                return 59 <= value <= 76
            if metric == "cm":
                return 150 <= value <= 193
        else:
            return False

    def validate_hcl(self, hcl):
        try:
            return re.match(r"#(([0-9]|[a-z]){6})", hcl).group(0) == hcl
        except:
            return False

    def validate_ecl(self, ecl):
        return ecl in ["amb", "blu", "brn", 'gry', "grn", "hzl", "oth"]

    def validate_pid(self, pid):
        try:
            return re.match(r"[0-9]{9}", pid).group(0) == pid
        except:
            return False


list_pprt = parse_data()
necessary_fields = {"iyr", "hgt", "byr", "pid", "eyr", "hcl", "ecl"}
validator = Validator()
valid_pprt = 0
for pprt in list_pprt:
    valid = True
    for field in necessary_fields:
        valid = valid and field in pprt.keys() and getattr(validator, f"validate_{field}")(pprt[field])
    if valid:
        valid_pprt +=1
print(valid_pprt)