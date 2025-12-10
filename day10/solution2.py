from aoutils import *
from collections import deque
import itertools
from z3 import *

lines = get_lines_splitted("machines.txt", " ")


target_states = []
lengths = []
transitions_list = []
transitions_vecs_list = []

for line in lines:
    target = line[-1][1:-1].split(",")
    rep = []
    for i, elem in enumerate(target):
        rep.append(int(elem))
    target_states.append(tuple(rep))
    current_len = len(rep)
    lengths.append(current_len)
    transitions = []
    transitions_vecs = []
    for _transitions in line[1:-1]:
        nums = _transitions[1:-1].split(",")
        nums = [int(num) for num in nums]
        transition_vec = [1 if i in nums else 0 for i in range(current_len)]
        transitions.append(nums)
        transitions_vecs.append(transition_vec)
    transitions_list.append(transitions)
    transitions_vecs_list.append(transitions_vecs)




def find_shortest_path(target, trans):
    v = []
    for l in range(len(trans)):
        v.append(Int(l))
    opt = Optimize()
    for i, val in enumerate(target):
        idx = []
        for j, elem in enumerate(trans):
            if i in elem:
                idx.append(j)
        opt.add(sum([x for k, x in enumerate(v) if k in idx]) == val)
    
    for var in v:
        opt.add(var >= 0)
    
    opt.minimize(sum(v))
    if opt.check() == sat:
        m = opt.model()
        s = 0
        for var in v:
            s += m[var].as_long()
        return s
    else:
        print("Keine Lösung")



num = 0
for target, length, trans, trans_vec in zip(target_states, lengths, transitions_list, transitions_vecs_list):
    print("start")
    num += find_shortest_path(target, trans)

print(num)