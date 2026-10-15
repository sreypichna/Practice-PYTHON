def clamp_speed(value, min_speed=0, max_speed=100):
    if value < min_speed:
        return min_speed
    elif value > max_speed:
        return max_speed
    else:
        return value
 
print(clamp_speed(150))
print(clamp_speed(-20))
print(clamp_speed(150, max_speed=200))