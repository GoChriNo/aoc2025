
commands = []
with open("rotation.txt", "r") as file:
    for line in file:
        line = line.strip()
        direction = line[0]
        value = int(line[1:])
        commands.append((direction, value))


pointer = 50
count = 0
print(commands)

for dir, val in commands:
    if dir == "R":
        pointer += val
    else:
        pointer -= val
    pointer = pointer % 100
    if pointer == 0:
        count += 1

print(count)