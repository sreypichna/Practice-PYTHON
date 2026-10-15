def cm_to_inch(cm):
    return cm / 2.54
 
def convert_all(readings):
    converted = []
    for r in readings:
        converted.append(cm_to_inch(r))
    return converted
 
raw = [10, 25.4, 50]
print(convert_all(raw))
