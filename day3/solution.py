lines = []
with open("batteries.txt", "r") as file:
    for line in file:
        lines.append(line.strip())



def get_best_digit(line, last_digit=False):
    first_encounter = {}
    num_batteries = len(line)
    for i, battery in enumerate(line):
        if battery not in first_encounter:
            first_encounter[battery] = i
            
    for digit in "987654321":
        if digit not in first_encounter:
            continue
        if first_encounter[digit] != num_batteries - 1 or last_digit:
            return first_encounter[digit]
    return num_batteries - 1


sum_joltage = 0

for line in lines:
    first_index = get_best_digit(line)
    seconde_index = get_best_digit(line[first_index+1:], last_digit=True)
    combined = line[first_index] + line[first_index + 1 + seconde_index]
    sum_joltage += int(combined)

print(sum_joltage)