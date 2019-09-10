import re
import ToyRobot

# Entry point of program. This file is where user input functionality is provided

command = ''
robot = ToyRobot.Robot()
is_placed = False
regex = re.compile(r'^PLACE\s[0-5][,][0-5][,](NORTH|SOUTH|EAST|WEST)')  # uses regex to enforce valid PLACE input
regex_placed = re.compile(r'^PLACE\s[0-5][,][0-5]')

while True:
    command = input("Enter an instruction for robot to execute: ")
    if command == 'QUIT':
        break
    if not is_placed:
        if regex.match(command):  # If the command matches the format PLACE X,X,DIRECTION
            is_placed = True  # Flag allows other commands to be executed
            coords = re.findall('\d+', command)  # Retrieve the coordinates X,X from the command input
            start_direction = command.rsplit(',', 1)[1]  # Retrieve the starting DIRECTION from the command input
            robot.place(int(coords[0]), int(coords[1]), start_direction)
        else:
            print("Invalid input. Use the place command to place robot"
                  " with the format 'PLACE X,X,DIRECTION' where X is between 0 and 5 inclusive and DIRECTION is one of "
                  "NORTH/SOUTH/EAST/WEST")
            continue
    else:
        if regex.match(command):
            coords = re.findall('\d+', command)
            start_direction = command.rsplit(',', 1)[1]
            robot.place(int(coords[0]), int(coords[1]), start_direction)
        elif regex_placed.match(command):
            coords = re.findall('\d+', command)
            robot.place(int(coords[0]), int(coords[1]))
        elif command == 'MOVE':
            robot.move()
        elif command == 'LEFT':
            robot.rotate('LEFT')
        elif command == 'RIGHT':
            robot.rotate('RIGHT')
        elif command == 'REPORT':
            print(robot.report())
        else:
            print("Invalid command. Valid commands are: PLACE X,X,DIRECTION or X,X if already placed (X between 0-5 inclusive, DIRECTION is "
                  " one of NORTH/SOUTH/EAST/WEST, MOVE, LEFT, RIGHT, REPORT")
