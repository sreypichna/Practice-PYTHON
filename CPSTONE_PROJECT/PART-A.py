def battery_after_move(current_battery, distance, drain_rate=0.5):
    return current_battery - (distance * drain_rate)
print(battery_after_move(100, 12))