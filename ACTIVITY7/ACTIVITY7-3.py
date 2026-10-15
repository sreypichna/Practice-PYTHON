readings = [12.0, 18.5, 9.0]
distance = 22
battery = 27

def average(values):
    if not values:
        return 0
    return sum(values) / len(values)

def is_safe_distance(distance, threshold=15):
    return distance >= threshold

def describe_battery(percent):
    if percent < 10:
        return 'CRITICAL'
    elif percent < 30:
        return 'LOW'
    elif percent < 80:
        return 'OK'
    else:
        return 'FULL'

print(f"Average distance: {average(readings):.2f}")
print(f"Safe to proceed: {is_safe_distance(distance)}")
print(f"Battery status: {describe_battery(battery)}")