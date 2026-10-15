queue = [12.4, None, 8.0, None, 30.1]
readings_used = 0
 
while queue:                       # keep going while the queue still has items
    reading = queue.pop(0)
    if reading is None:
        continue                       # skip noisy readings, don't count them
    readings_used += 1
    print(f"Processed: {reading} cm")
 
print(f"Valid readings used: {readings_used}")
