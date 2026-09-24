import heapq

with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.read().split(',')


def format_state(unformatted_state):
    values = [int(x.strip()) for x in unformatted_state[:4]]
    boat = 0 if unformatted_state[4].strip() == 'L' else 1
    return tuple(values + [boat])


def unformat_state(state):
    ml, cl, mr, cr, boat = state
    return f"{ml}, {cl}, {mr}, {cr}, {'L' if boat == 0 else 'R'}"


start_state = format_state(lines)
GOAL_STATE = (0, 0, 3, 3, 1)
MOVES = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]


def next_state(current_state, m, c):
    ml, cl, mr, cr, boat = current_state
    dir = 1 if boat == 0 else -1
    return (ml - dir * m, cl - dir * c, mr + dir * m, cr + dir * c, 1 - boat)


def is_valid(state):
    ml, cl, mr, cr, _ = state
    if min(ml, cl, mr, cr) < 0:
        return False
    if ml > 0 and cl > ml:
        return False
    if mr > 0 and cr > mr:
        return False
    return True


def successors(state):
    results = []
    for m, c in MOVES:
        next_s = next_state(state, m, c)
        if is_valid(next_s):
            results.append((next_s, 1))
    return results


def h1(state):
    ml, cl, mr, cr, boat = state
    return 2 * ml + cl


def h2(state):
    ml, cl, mr, cr, boat = state
    return (2 * ml + cl + 2) // 3


def h3(state):
    ml, cl, mr, cr, boat = state
    remaining_people = ml + cl
    remaining_weight = 2 * ml + cl

    if remaining_people == 0:
        return 0
    if boat == 0 and remaining_people <= 2:
        return remaining_weight
    return remaining_weight + 1


def check_consistency(states, heuristic):
    for state in states:
        for next_state, cost in successors(state):
            if heuristic(state) > cost + heuristic(next_state):
                return False
    return True


def generate_states(start):
    seen = set()
    queue = [start]
    while queue:
        state = queue.pop(0)
        if state in seen:
            continue
        seen.add(state)
        for next_state, _ in successors(state):
            if next_state not in seen:
                queue.append(next_state)
    return seen


def astar(start, heuristic):
    open_heap = [(heuristic(start), 0, start)]
    g_score = {start: 0}
    came_from = {start: None}
    expansions = 0
    closed = set()

    while open_heap:
        _, g_val, current = heapq.heappop(open_heap)
        if current in closed:
            continue

        closed.add(current)
        expansions += 1

        if current == GOAL_STATE:
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = came_from[node]
            path.reverse()
            return {
                'path': path,
                'cost': g_val,
                'expansions': expansions,
            }

        for next_state, cost in successors(current):
            tentative_cost = g_val + cost
            if tentative_cost < g_score.get(next_state, float('inf')):
                g_score[next_state] = tentative_cost
                came_from[next_state] = current
                priority = tentative_cost + heuristic(next_state)
                heapq.heappush(open_heap, (priority, tentative_cost, next_state))

    return None


heuristics = {
    'h1': h1,
    'h2': h2,
    'h3': h3,
}

state_space = generate_states(start_state)

for name, heuristic in heuristics.items():
    result = astar(start_state, heuristic)
    consistent = check_consistency(state_space, heuristic)
    print(f"Heuristic {name} is consistent: {consistent}")
    if result is None:
        print(f"The solution of Q3.1 ({name}) is: No solution")
        continue

    path_h = " -> ".join(unformat_state(step) for step in result['path'])
    print(f"The solution of Q3.1 ({name}) is:")
    print(f"Solution Path: {path_h}")
    print(f"Total cost = {result['cost']}")
    print(f"Number of node expansions = {result['expansions']}")
    print()