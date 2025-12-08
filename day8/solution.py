from aoutils import *
from unionfind import UnionFind

boxes = get_lines_splitted("boxes.txt", ",")

boxes = [[int(coord) for coord in box] for box in boxes]


distances = {}


def get_distance(coords1, coords2):
    connection = (coords1[0] - coords2[0], coords1[1] - coords2[1], coords1[2] - coords2[2])
    return (connection[0]**2 + connection[1]**2 + connection[2]**2)**0.5


for i in range(len(boxes)):
    for j in range(i+1, len(boxes)):
        distances[(i,j)] = get_distance(boxes[i], boxes[j])

distances_sorted = sorted(distances.items(), key=lambda x: x[1])


uf = UnionFind()
for i in range(len(boxes)):
    uf.add(i)


for k in range(1000):
    index, distance = distances_sorted[k]
    i, j = index
    uf.union(i, j)

sets = uf.get_sets()
set_sizes = [len(x) for x in sets]
set_sizes_sorted = sorted(set_sizes)[::-1]
print(set_sizes_sorted[0] * set_sizes_sorted[1] * set_sizes_sorted[2])
