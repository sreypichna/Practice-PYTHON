import types
UserInput = types.SimpleNamespace()
UserInput.commands = ["forward", "left", "jump", "stop", "quit"]
move_counter = 0
while True:
    command = input("Command (forward/left/jump/stop/quit): ")
    if command in UserInput.commands[:-1]:  
        print(f"Executing: {command.upper()}")
        move_counter += 1
    elif command == "quit":
        print("Session ended.")
        break
    else:
        print("Unknown command, try again.")
print(f"Total moves: {move_counter}")
        
