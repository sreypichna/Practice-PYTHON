left_sees_line = True
center_sees_line = False
right_sees_line = False
 
if not left_sees_line and not center_sees_line and not right_sees_line:
    move = "STOP"          # lost the line completely
elif left_sees_line and not right_sees_line:
    move = "TURN LEFT"     # drifted right, line is on the left sensor
elif right_sees_line and not left_sees_line:
    move = "TURN RIGHT"    # drifted left, line is on the right sensor
else:
    move = "GO"             # centered on the line
 
print(f"Move: {move}")
