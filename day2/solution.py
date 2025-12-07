
id_ranges = []

with open("ids.txt", "r") as file:
    for line in file:
        ranges = line.strip().split(",")
        for _range in ranges:
            range_split = _range.split("-")
            id_ranges.append((int(range_split[0]), int(range_split[1])))


def is_valid(id):
    id_str = str(id)
    id_digits = len(id_str)
    if id_digits % 2 == 1:
        return True
    if id_str[:id_digits//2] == id_str[id_digits//2:]:
        return False
    return True


sum_invalid = 0

for start, end in id_ranges:
    for id in range(start, end+1, 1):
        if not is_valid(id):
            sum_invalid += id

print(sum_invalid)