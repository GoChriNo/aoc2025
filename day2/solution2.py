
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

    for i in range(1, id_digits // 2 + 1):
        num_fits = id_digits / i
        if num_fits != id_digits // i:
            continue
        num_fits = id_digits // i
        repeater = id_str[:i]
        for j in range(1, num_fits):
            if id_str[i*j:i*(j+1)] != repeater:
                break
        else:
            return False
    return True


sum_invalid = 0

for start, end in id_ranges:
    for id in range(start, end+1, 1):
        print("id: ", id, " is valid: ", is_valid(id))
        if not is_valid(id):
            sum_invalid += id

print(sum_invalid)