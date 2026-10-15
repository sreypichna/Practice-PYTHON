speeds = [0.0, 0.8, 1.5, 2.0, 2.4, 2.2, 1.6, 0.5]
print(f"t=0.0s -> {speeds[0]} m/s")
print("... (one line per reading) ...")
print(f"Average speed: {round(sum(speeds) / len(speeds), 2)} m/s")
print(f"Fastest: {max(speeds)} m/s at t={speeds.index(max(speeds)) * 0.5}s")
start_segment = speeds[:3]
finish_segment = speeds[-3:]
print(f"Start segment: {start_segment}")
print(f"Finish segment: {finish_segment}")