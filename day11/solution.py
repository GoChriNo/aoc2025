from aoutils import * 

lines = get_lines_splitted("cables.txt", " ")

graph = {}

for line in lines:
    graph[line[0][:-1]] = line[1:]

def t_order(order, graph, vert):
    if vert in order:
        return
    if vert in graph:
        for neighbor in graph[vert]:
            t_order(order, graph, neighbor)
    order.append(vert)

order = []
t_order(order, graph, "you")

paths = {}
paths["you"] = 1
for vert in order[::-1]:
    if vert not in graph:
        continue
    for neighbor in graph[vert]:
        paths[neighbor] = paths.get(neighbor, 0) + paths[vert]

print(paths["out"])