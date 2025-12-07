
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





unique_ranges = []
while len(fresh_ranges) > 0:
    print(len(fresh_ranges))
    print(fresh_ranges)
    for start, end in fresh_ranges[:]:
        for i, (s, e) in enumerate(unique_ranges[:]):
            start_ib = False
            end_ib = False
            over = False
            if start >= s and start <= e:
                start_ib = True
            if end >= s and end <= e:
                end_ib = True
            if s > start and e < end:
                over = True

            if start_ib and end_ib:
                fresh_ranges.remove((start, end))
                break
            elif start_ib or end_ib or over:
                new_start = start
                new_end = end
                if start_ib:
                    new_start = s
                if end_ib:
                    new_end = e
                fresh_ranges.append((new_start, new_end))
                unique_ranges.pop(i)
                break
        else:
            unique_ranges.append((start, end))
            fresh_ranges.remove((start, end))


count = 0
for start, end in unique_ranges:
    count += (end - start + 1)

print(count)
