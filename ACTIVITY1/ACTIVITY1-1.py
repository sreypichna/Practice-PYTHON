MAX_BATTERY = 8.4  # volts, constant for this robot model
 
robot_name = "bumblebee"
battery_voltage = 7.1
x_pos, y_pos = 3, 5   # multiple assignment
 
battery_percent = round(battery_voltage / MAX_BATTERY * 100, 1)
 
print(f"Robot: {robot_name.title()}")
print(f"Position: ({x_pos}, {y_pos})")
print(f"Battery: {battery_percent}% of {MAX_BATTERY}V max")
