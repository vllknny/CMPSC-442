state = (3, 3, 0, 0, 0)
MOVES = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]

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
        

def dfs(state, path, visited):
    if state == (0, 0, 3, 3, 1):
        return path
    visited.add(state)
    for s in next_states(state):
        if s not in visited:
            result = dfs(s, path + [s], visited)
            if result is not None:
                return result
    return None

solution = dfs(state, [state], set())
for step in solution:
    print(step)