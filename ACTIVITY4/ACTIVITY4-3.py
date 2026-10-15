signal_color = "green"
pedestrian_pressed = True
if signal_color == "red" or pedestrian_pressed:
    action = "STOP"
    print(f"Action: {action}")
if signal_color == "yellow":
    action = "SLOW DOWN, PREPARE TO STOP"
    print(f"Action: {action}")
if signal_color == "green" and not pedestrian_pressed:
    action = "GO"
    print(f"Action: {action}")
if signal_color == "green" and pedestrian_pressed:
    action = "SLOW DOWN, PREPARE TO STOP"
    print(f"Action: {action}")
if signal_color not in ["red", "yellow", "green"]:
    print("ERROR: UNKNOWN SIGNAL")