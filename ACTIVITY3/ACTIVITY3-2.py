scores = [145, 210, 98, 176, 210]
total = sum(scores)
average = round(total / len(scores), 1)
best = max(scores)
worst = min(scores)

print(f"Total: {total} | Average: {average}")
print(f"Best: {best} | Worst: {worst}")
