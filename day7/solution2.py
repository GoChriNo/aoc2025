from aoutils import *
from collections import deque

space = get_value_grid("space.txt", 0)

space.set_oob_symbol("#")

start_pos = space.find_symbol("S")
start_pos.value = 1

laser_queue = deque()

laser_queue.append(start_pos)

while len(laser_queue) > 0:
    pos = laser_queue.popleft()
    next_space = pos.down
    if next_space.symbol in [".", "|"]:
        next_space.symbol = "|"
        next_space.value += pos.value
        if next_space not in laser_queue:
            laser_queue.append(next_space)
    elif next_space.symbol == "^":
            next_space.left.symbol = "|"
            next_space.left.value += pos.value
            if next_space.left not in laser_queue:
                laser_queue.append(next_space.left)

            next_space.right.symbol = "|"
            next_space.right.value += pos.value
            if next_space.right not in laser_queue:
                laser_queue.append(next_space.right)

count = 0
for pos in space.get_row(space.dim_y - 1):
    count += pos.value

print(count)