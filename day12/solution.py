from aoutils import *

lines = get_lines_splitted("input.txt")


challenges = []
gifts = {}
i = 0
while i < len(lines):
    line = lines[i]
    if len(line) > 1:
        size = line[0][:-1]
        challenges.append((size, line[1:]))
        i += 1
    else:
        gifts[len(gifts)] = sum([s.count("#") for curr_line in [lines[i+1], lines[i+2], lines[i+3]] for s in curr_line])
        i += 5

count_fitting = 0

for size, nums in challenges:
    size = size.split("x")
    size = int(size[0]) * int(size[1])
    gift_size = 0
    for i, num in enumerate(nums):
        gift_size += int(num) * gifts[i]
    if gift_size <= size:
        count_fitting += 1

print(count_fitting)
    