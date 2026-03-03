def vacuum_agent(location, status):
    if status == "Dirty":
        return "Suck"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"

# Environment simulation
rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"

for _ in range(4):
    action = vacuum_agent(location, rooms[location])
    print(f"Location: {location}, Status: {rooms[location]}, Action: {action}")

    if action == "Suck":
        rooms[location] = "Clean"
    elif action == "Move Right":
        location = "B"
    elif action == "Move Left":
        location = "A"
