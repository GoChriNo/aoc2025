
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
    start = pointer
    if dir == "R":
        pointer += val
    else:
        pointer -= val
    count += abs((pointer // 100))
    tmp = pointer
    pointer = pointer % 100
    if 0 == (pointer % 100) and tmp <= 0:
        count += 1
    if 0 == start and dir == "L":
        count -= 1
    print(dir, val)
    print(pointer)
    print("count", count)
    #if pointer == 0:
    #    count += 1

print(count)