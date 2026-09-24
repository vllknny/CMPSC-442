state = (3, 3, 0, 0, 0)
boat_is_left = "L" if state[4] == 0 else "R"
stack = []

def next_state(current_state, m, c): 
    new_state = list(current_state)
    ml, cl, mr, cr, boat = new_state
    d = 1 if boat == 0 else -1

    return (ml - d*m,  cl - d*c, mr + d*m, cr + d*c, 1 - boat)


    

