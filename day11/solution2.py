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
t_order(order, graph, "svr")

paths = {}
paths["svr"] = (1, 0)
for vert in order[::-1]:
    if vert not in graph:
        continue
    for neighbor in graph[vert]:
        vert_paths, vert_state = paths[vert]
        if neighbor not in paths:
            paths[neighbor] = (0,0)
        neighbor_paths, neighbor_state = paths[neighbor]
        
        if neighbor in ["fft", "dac"]:
            vert_state += 1

        if vert_state > neighbor_state:
            paths[neighbor] = (vert_paths, vert_state)
        elif vert_state < neighbor_state:
            paths[neighbor] = (neighbor_paths, neighbor_state)
        else:
            paths[neighbor] = (neighbor_paths + vert_paths, vert_state)
        

print(paths["out"])