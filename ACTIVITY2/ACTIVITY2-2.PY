readings = [42.5, 30.1, 55.0, 18.7]
 
readings.append(12.3)                  # a new reading just came in
 
most_recent = readings[-1]
closest = sorted(readings)[0]   # sort a copy, keep 'readings' untouched

print(f"Most recent reading: {most_recent} cm")
print(f"Closest object so far: {closest} cm")
print(f"Original order preserved: {readings}")
