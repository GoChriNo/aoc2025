
fresh_ranges = []
ids = []

with open("ids.txt", "r") as file:
    state = 0
    for line in file:
        if state == 0:
            if len(line.strip()) == 0:
                state = 1
                continue
            splitted = line.strip().split("-")
            fresh_ranges.append((int(splitted[0]), int(splitted[1])))
        else:
            ids.append(int(line.strip()))

count = 0

for id in ids:
    for start, end in fresh_ranges:
        if id >= start and id <= end:
            count += 1
            break

print(count)