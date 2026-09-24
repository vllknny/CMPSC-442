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
    successors = {}
    for m, c in MOVES:
        s = next_state(state, m, c)
        if is_valid(s):
            successors[s] = (m, c)
    return successors

def cost(state, move, model):
    ml, cl, mr, cr, boat = state
    m, c = move
    if model == 'A':
        return MISSIONARY_COST*m + CANNIBAL_COST*c
    return 2 if boat == 0 else 1  

        

def ucs(start, model):
    pq = [(0, start, [start])]         
    visited = set()

    while pq:
        g, current, path = heapq.heappop(pq)    

        if current == (0, 0, 3, 3, 1):         
            return path, g
        if current in visited:                 
            continue
        
        visited.add(current)
        node_exp[0] += 1                      

        for s, move in next_states(current).items():   
            if s not in visited:
                new_g = g + cost(current, move, model)  
                heapq.heappush(pq, (new_g, s, path + [s]))  

    return None, None 

for model in ['A', 'B']:
    node_exp[0] = 0
    solution, total = ucs(state, model)
    print(f"The solution of Q2.1 (UCS, cost model {model}) is:")
    if solution == None: 
        print("No solution")
    else: 

        print("Solution Path: ")
        for step in solution:
            print(unformat_state(step))

        print(f"Total cost = {total}")
        print(f"Number of node expansions = {node_exp[0]}")
    print()
