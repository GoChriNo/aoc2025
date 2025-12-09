from aoutils import *

tiles = get_lines_splitted("tiles.txt", ",")


def get_area(coords1, coords2):
    x1, y1 = coords1
    x1, y1 = int(x1), int(y1)
    x2, y2 = coords2
    x2, y2 = int(x2), int(y2)
    return (abs(x1 - x2) + 1) * (abs(y1 -y2) + 1)


max_area = 0

for i in range(len(tiles)):
    for j in range(i + 1, len(tiles)):
        area = get_area(tiles[i], tiles[j])
        if area > max_area:
            max_area = area

print(max_area)