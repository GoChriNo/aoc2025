lines = []
with open("batteries.txt", "r") as file:
    for line in file:
        lines.append(line.strip())



def get_best_digit(line, start_index, digits_left):
    first_encounter = {}
    num_batteries = len(line)
    for i, battery in enumerate(line):
        if i < start_index or i >= num_batteries - digits_left:
            continue
        if battery not in first_encounter:
            first_encounter[battery] = i
            
    for digit in "987654321":
        if digit not in first_encounter:
            continue
        return digit, first_encounter[digit]
    return None


sum_joltage = 0

for line in lines:
    digits = ""
    start = 0
    for i in range(11, -1, -1):
        digit, index = get_best_digit(line, start, i)
        digits += digit
        start = index + 1
    sum_joltage += int(digits)

print(sum_joltage)