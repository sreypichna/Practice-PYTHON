# Goal: Drive the robot down the corridor one room at a time using a while loop, stopping early if power runs out.
# 1. Use a while loop (with an index or a shrinking copy of the list) to visit rooms in order, one at a time.
# 2. For each room: print its id and the result of classify_room(room).
# 3. Update robot_state["battery"] using battery_after_move(...) with that room's distance, then increase robot_state["moves"] by 1.
# 4. If robot_state["battery"] drops below 20 at any point, immediately print "MISSION ABORTED - LOW BATTERY" and break out of the loop — do not visit any further rooms.
robot_state = {"battery": 100, "moves": 0}
rooms = [ 
    {"id": 1, "distance": 5, "hazard": False, "survivor": False},
    {"id": 2, "distance": 10, "hazard": True, "survivor": False},
    {"id": 3, "distance": 8, "hazard": False, "survivor": True},
    {"id": 4, "distance": 12, "hazard": False, "survivor": False},
]
battery_after_move = lambda current_battery, distance, drain_rate=0.5: current_battery - (distance * drain_rate)
classify_room = lambda room: "HAZARD - SKIP" if room["hazard"] else ("SURVIVOR FOUND" if room["survivor"] else "CLEAR - NO SURVIVOR")
while robot_state["battery"] >= 20 and rooms:
    room = rooms.pop(0)
    print(f"Visiting room {room['id']}: {classify_room(room)}")
    robot_state["battery"] = battery_after_move(robot_state["battery"], room["distance"])
    robot_state["moves"] += 1

if robot_state["battery"] < 20:
    print("MISSION ABORTED - LOW BATTERY")