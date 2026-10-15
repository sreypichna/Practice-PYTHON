distance_cm = 22
battery_percent = 12
 
if battery_percent < 15:
    action = "RETURN_TO_BASE"
elif distance_cm < 10:
    action = "STOP"
elif distance_cm < 30:
    action = "SLOW"
else:
    action = "GO"
 
print(f"Action: {action}")
