from collections import deque

initial_state = ('door', 'window', False, False)
positions = ['door', 'window', 'middle']

def get_successors(state):
    monkey_pos, box_pos, on_box, has_banana = state
    successors = []

    if has_banana:
        return successors

    if not on_box:
        for pos in positions:
            if pos != monkey_pos:
                successors.append((pos, box_pos, False, False))

    if not on_box and monkey_pos == box_pos:
        for pos in positions:
            if pos != box_pos:
                successors.append((pos, pos, False, False))

    if monkey_pos == box_pos and not on_box:
        successors.append((monkey_pos, box_pos, True, False))

    if monkey_pos == 'middle' and box_pos == 'middle' and on_box:
        successors.append((monkey_pos, box_pos, True, True))

    return successors


def bfs():
    queue = deque()
    queue.append((initial_state, []))
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue
        visited.add(state)

        if state[3]:
            return path + [state]

        for successor in get_successors(state):
            queue.append((successor, path + [state]))

    return None


solution = bfs()

if solution:
    for step in solution:
        print(step)
else:
    print("No solution found.")
