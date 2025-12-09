from aoutils import *

from collections import defaultdict

tiles = get_lines_splitted("tiles.txt", ",")


def get_area(coords1, coords2):
    x1, y1 = coords1
    x1, y1 = int(x1), int(y1)
    x2, y2 = coords2
    x2, y2 = int(x2), int(y2)
    return (abs(x1 - x2) + 1) * (abs(y1 -y2) + 1)

for i, tile in enumerate(tiles):
    tiles[i][0], tiles[i][1] = int(tile[0]), int(tile[1])

# dict that holds x values for every y value (horizontal slices)
floor = defaultdict(list)


#set red tiles and connect them
for i, tile in enumerate(tiles):
    floor[tile[1]].append(tile[0])
    last_tile = tiles[i-1]
    if last_tile[0] == tile[0]:
        index = 1
    elif last_tile[1] == tile[1]:
        index = 0
    diff = tile[index] - last_tile[index]
    it = range(1, diff)
    if diff < 0:
        it = range(-1, diff, -1)
    if index == 0:
        for k in it:
            floor[tile[1]].append(last_tile[0] + k)
    else:
        for k in it:
            floor[last_tile[1] + k].append(tile[0])


# creating of valid ranges dict (holds ranges that are in the valid area as horizontal slices)
valid_ranges = defaultdict(list)
for y in floor.keys():
    floor[y] = sorted(floor[y])

    curr_start = floor[y][0]
    last_elem = floor[y][0]
    phase = 0
    for i in range(1, len(floor[y])):
        if phase == 0:
            if floor[y][i] == last_elem + 1:
                last_elem = floor[y][i]
            else:
                last_elem = floor[y][i]
                phase = 1
        else:
            if floor[y][i] == last_elem + 1:
                last_elem = floor[y][i]
            else:
                valid_ranges[y].append((curr_start, last_elem))
                curr_start = floor[y][i]
                last_elem = floor[y][i]
                phase = 0
    valid_ranges[y].append((curr_start, last_elem))


def is_valid(tile1, tile2, valid_ranges):
    diff_y = tile1[1] - tile2[1]
    it2 = range(0, diff_y + 1)
    if diff_y < 0:
        it2 = range(0, diff_y - 1, -1)
        
    for y_offset in it2:
        for valid_range in valid_ranges[tile2[1] + y_offset]:
            start_x = tile1[0]
            end_x = tile2[0]
            if end_x < start_x:
                start_x, end_x = end_x, start_x
            if start_x >= valid_range[0] and end_x <= valid_range[1]:
                break
        else:
            return False
            
    return True

areas = []

for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        area = get_area(tiles[i], tiles[j])
        areas.append((area, tiles[i], tiles[j]))

count = 0
for area, tile1, tile2 in sorted(areas, key=lambda x: x[0])[::-1]:
    if count % 2500 == 0:
        print(count / len(areas))
    count += 1
    if is_valid(tile1, tile2, valid_ranges):
        print(area)
        break