import heapq

# Goal State
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Heuristic Function (Manhattan Distance)
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x = (value - 1) // 3
                goal_y = (value - 1) % 3
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance


# Find position of blank (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


# Generate possible moves
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors


# A* Algorithm
def a_star(start):
    open_list = []
    heapq.heappush(open_list, (heuristic(start), 0, start, []))
    visited = set()

    while open_list:
        f, g, current, path = heapq.heappop(open_list)

        if str(current) in visited:
            continue
        visited.add(str(current))

        if current == goal_state:
            return path + [current]

        for neighbor in get_neighbors(current):
            heapq.heappush(open_list, (
                g + 1 + heuristic(neighbor),
                g + 1,
                neighbor,
                path + [current]
            ))

    return None


# Initial State
start_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

# Solve
solution = a_star(start_state)

# Output
if solution:
    print("\n8-Puzzle Solution (Using A* with Manhattan Distance):\n")
    step = 1
    for state in solution:
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()
        step += 1
else:
    print("No solution found.")
