detected = [88.0, 240.5, 15.2, 60.0, 199.9]
detected.insert(0, 5.0)
cleaned = []
for d in detected:
    if d <= 200:
        cleaned.append(d)
cleaned.sort()
print(f"Cleaned & sorted distances: {cleaned}")
print(f"Closest obstacle: {cleaned[0]} cm")
