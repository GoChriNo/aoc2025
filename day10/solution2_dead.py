from aoutils import *
from collections import deque
import itertools

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



def compositions(n, x):
    for bars in itertools.combinations(range(n + x - 1), x - 1):
        parts = []
        prev = -1
        for b in bars:
            parts.append(b - prev - 1)
            prev = b
        parts.append(n + x - 1 - prev - 1)
        yield tuple(parts)


def add_vecs(vec1, vec2):
    return tuple([x + y for x, y in zip(vec1, vec2)])

def add_vecs_n(vec1, vec2, n):
    return tuple([x + n*y for x, y in zip(vec1, vec2)])


def count_n(t, l):
    count = [0] * length
    for elem in t:
        for num in elem:
            count[num] += 1
    for i in range(len(count)):
        if count[i] <= 0:
            count[i] = float("+inf")
    return count

def find_shortest_path(target, transistions, transition_vecs, length):
    l = length
    t = transistions.copy()
    t_vec = transition_vecs.copy()
    possible_points = {}
    possible_points[(0,) * length] = 0
    print("target: ", target)
    changed = False
    while True:
        #print("t", t)
        count = count_n(t, l)
        i = count.index(min(count))
        n = min(count)

        if n == float("+inf"):
            break
        min_next = float("+inf")
        min_target = float("+inf")
        min_target_index = 0
        print("count: ", count, i)
        for k, elem in enumerate(count):
            if elem != n:
                continue
            if target[k] < min_target:
                min_target = target[k]
                min_target_index = k
            not_idx = [j for j, elem in enumerate(t) if k not in elem]
            tmp = [t[j] for j in not_idx]
            count2 = count_n(tmp, l)
            print("c2", count2)
            if min(count2) < min_next:
                min_next = min(count2)
                i = k
        #print("starting reduction for :", i)
        print(n)
        print(i)

        idx = [j for j, elem in enumerate(t) if i in elem]
        not_idx = [j for j, elem in enumerate(t) if i not in elem]
        curr_t = [t[j] for j in idx]
        #print("curr_t", curr_t)
        curr_t_vec = [t_vec[j] for j in idx]
        
        goal = target[i]
        reachable = {}
        print("current possible points:", len(possible_points))
        cc = 0
        for point, steps in possible_points.items():
            cc += 1
            if cc % 100 == 0:
                print(cc/len(possible_points))
            for comb in compositions(goal - point[i], n):
                vec = (0,) * l
                for j, c in enumerate(comb):
                    vec = add_vecs_n(vec, curr_t_vec[j], c)
                    new_point = add_vecs(point, vec)
                if not any([x > y for x, y in zip(new_point, target)]):
                    if new_point not in reachable or reachable[new_point] > steps + goal - point[i]:
                        reachable[new_point] = steps + goal - point[i]
                    changed = True
        
        t = [t[j] for j in not_idx]
        t_vec = [t_vec[j] for j in not_idx]

        if not changed:
            break
        else:
            possible_points = reachable



    min_steps = float("+inf")
    for elem, steps in possible_points.items():
        if elem == target and steps < min_steps:
            min_steps = steps

    return min_steps

    
            

                


num = 0
for target, length, trans, trans_vec in zip(target_states, lengths, transitions_list, transitions_vecs_list):
    print("start")
    num += find_shortest_path(target, trans, trans_vec, length)

print(num)