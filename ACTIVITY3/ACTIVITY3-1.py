speeds = [0.0, 1.2, 2.5, 2.4, 2.6, 1.0]
 
for i in range(len(speeds)):
    time = i * 0.5
    print(f"t={time}s -> {speeds[i]} m/s")
print(f"Average speed: {round(sum(speeds) / len(speeds), 2)} m/s")
