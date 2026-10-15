name = "scout"
team_number = 7
voltage = 1.5   # out of 8.4V max
MAX_BATTERY = 8.4
battery_percentage = round(voltage / MAX_BATTERY * 100, 1)
print(f"[TEAM{team_number:02d}] {name.upper()} - {battery_percentage}% PWR")
if battery_percentage < 20:
    print("⚠ LOW POWER — RETURN TO BASE")