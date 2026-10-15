fleet = {
    "rex":    {"battery": 18, "position": (2, 3), "status": "ACTIVE"},
    "scout":  {"battery": 74, "position": (5, 1), "status": "IDLE"},
    "atlas":  {"battery": 55, "position": (0, 0), "status": "ACTIVE"},
}
for name, data in fleet.items():
    if data["battery"] < 20:
        print(f"ALERT: {name} battery critical ({data['battery']}%)")

active_robots = 0
idle_robots = 0
highest_battery = -1
highest_battery_robot = None

for name, data in fleet.items():
    if data["status"] == "ACTIVE":
        active_robots += 1
    elif data["status"] == "IDLE":
        idle_robots += 1

    if data["battery"] > highest_battery:
        highest_battery = data["battery"]
        highest_battery_robot = name

print(f"Active robots: {active_robots} | Idle robots: {idle_robots}")
print(f"Highest battery: {highest_battery_robot}")