
route = ["A1", "B2", "C3", "D4"]
 
print(f"First stop: {route[0]}")
print(f"Final stop: {route[-1]}")
 
route.append("E5")          # add a new final stop
route.remove("B2")         # skip a blocked waypoint
 
print(f"Updated route ({len(route)} stops): {route}")
