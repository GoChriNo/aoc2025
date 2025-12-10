from aoutils import *
from collections import deque

lines = get_lines_splitted("machines.txt", " ")


target_states = []
lengths = []
transitions_list = []

for line in lines:
    target = line[0][1:-1]
    rep = 0
    for i, elem in enumerate(target[::-1]):
        rep += 2**i if elem == "#" else 0
    target_states.append(rep)
    current_len = len(target)
    lengths.append(current_len)
    transitions = []
    for _transitions in line[1:-1]:
        nums = _transitions[1:-1].split(",")
        transitions.append(sum([2**(current_len - 1 - int(t)) for t in nums]))
    transitions_list.append(transitions)



def find_shortest_path(target, transistions, length):
    path_list = [float("+inf")] * (2**length)
    q = deque()
    q.append(0)
    path_list[0] = 0
    while len(q) >= 1:
        elem = q.popleft()
        curr_l = path_list[elem]
        for t in transistions:
            new_elem = elem ^ t
            new_l = curr_l + 1
            if path_list[new_elem] > new_l:
                path_list[new_elem] = new_l
                q.append(new_elem)

    return path_list[target]


num = 0
for target, length, trans in zip(target_states, lengths, transitions_list):
    num += find_shortest_path(target, trans, length)

print(num)