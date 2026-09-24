import heapq

with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.read().split(',')


def format_state(unformatted_state):
    return tuple([int(x.strip()) for x in unformatted_state[:4]] + [0 if unformatted_state[4].strip() == 'L' else 1])

def unformat_state(formatted): 
    temp = tuple([str(x) for x in formatted[:4]] + ['L' if formatted[4] == 0 else 'R'])
    return ", ".join(temp)

state = format_state(lines)

MOVES = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
MISSIONARY_COST = 2
CANNIBAL_COST = 1
node_exp = [0]

def next_state(current_state, m, c): 
    new_state = list(current_state)
    ml, cl, mr, cr, boat = new_state
    d = 1 if boat == 0 else -1

    return (ml - d*m,  cl - d*c, mr + d*m, cr + d*c, 1 - boat)

def is_valid(state):
    ml, cl, mr, cr, _ = state
    if (min(ml, cl, mr, cr) < 0) or (ml > 0 and cl > ml) or (mr > 0 and cr > mr): 
        return False
    return True

def next_states(state):
    successors = []
    for m, c in MOVES:
        s = next_state(state, m, c)
        if is_valid(s):
            successors.append(s)
    return successors
        

def ucs(state, path, visited):
    if state == (0, 0, 3, 3, 1):
        return path
    visited.add(state)
    node_exp[0]+=1
    for s in next_states(state):
        if s not in visited:
            result = dfs(s, path + [s], visited)
            if result is not None:
                return result
    return None

solution = ucs(state, [state], set())
print("The solution of Q1.1.a (DFS) is:")
if solution == None: 
    print("No solution")
else: 

    print("Solution Path: ")
    for step in solution:
        print(unformat_state(step))

    print(f"Total cost = {len(solution) - 1}")
    print(f"Number of node expansions = {node_exp[0]}")