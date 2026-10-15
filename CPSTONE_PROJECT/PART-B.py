def classify_room(room):
    if room["hazard"]:
        return "HAZARD - SKIP"
    elif room["survivor"]:
        return "SURVIVOR FOUND"
    else:
        return "CLEAR - NO SURVIVOR"

room1 = {"hazard": True, "survivor": False}
print(classify_room(room1))  