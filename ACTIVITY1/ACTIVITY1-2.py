MAX_BATTERY = 12.0
current_voltage = 9.6
 
percent_left = current_voltage / MAX_BATTERY * 100
percent_left = round(percent_left, 2)
 
status = "team_falcon"
 
print(f"[{status.upper()}] Battery at {percent_left}%")
