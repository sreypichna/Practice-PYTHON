robot = {
    "name": "rex",
    "max_speed": 2.5,
    "sensors": ["ultrasonic", "line", "gyro"],
    "battery": 91,
}
 
print(f"Sensor count: {len(robot['sensors'])}")
 
for key, value in robot.items():
    print(f"{key}: {value}")
