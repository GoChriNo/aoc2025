from aoutils import *
from collections import deque

space = get_grid("space.txt")

space.set_oob_symbol("#")

start_pos = space.find_symbol("S")

laser_queue = deque()

laser_queue.append(start_pos)

while len(laser_queue) > 0:
    pos = laser_queue.popleft()
    next_space = pos.down
    if next_space.symbol == ".":
        next_space.symbol = "|"
        laser_queue.append(next_space)
    elif next_space.symbol == "^":
        if next_space.left.symbol != "|":
            next_space.left.symbol = "|"
            laser_queue.append(next_space.left)
        if next_space.right.symbol not in ["|", "#"]:
            next_space.right.symbol = "|"
            laser_queue.append(next_space.right)


count = 0
for pos in space:
    if pos.symbol == "^" and pos.up.symbol == "|":
        count += 1

print(space)

print(count)