class Robot:

    direction = ['NORTH', 'EAST', 'SOUTH', 'WEST']
    min_pos = 0
    max_pos = 5
    direction_index = None
    obstacles = []
    place_flag = False

    def __init__(self, x=None, y=None, f=None, o=[]):
        self.x = x
        self.y = y
        self.f = f
        self.obstacles = o

    # Places robot on the grid. The use of regex to enforce valid input means that invalid coordinates cannot be passed
    # into the method. The invalid input guards are included in case of future modification.
    def place(self, x, y, f=None):
        if x < self.min_pos or x > self.max_pos:
            return "Invalid coordinates. Please enter x and y values between 0 and 5 inclusive"
        if y < self.min_pos or y > self.max_pos:
            return "Invalid coordinates. Please enter x and y values between 0 and 5 inclusive"
        if f not in self.direction and f != None:
            return "Invalid direction. Please enter a direction of NORTH, SOUTH, EAST OR WEST"
        if [x,y] in self.obstacles:
            return "Coordinates are designated to be avoided, please enter another location"
        self.x = x
        self.y = y
        if f == None:
            pass
        else:
            self.f = f
            self.direction_index = self.direction.index(self.f)  # tracks direction in the direction list
            self.place_flag = True


    def avoid(self, x, y):
        if x < self.min_pos or x > self.max_pos:
            print("Invalid coordinates. Please enter x and y values between 0 and 5 inclusive")
            return
        if y < self.min_pos or y > self.max_pos:
            print("Invalid coordinates. Please enter x and y values between 0 and 5 inclusive")
            return
        if x == self.x and y == self.y:
            print("Robot is in this location, invalid coordinates")
            return
        if [x,y] in self.obstacles:
            print("Cell is already designated to be avoided")
            return
        coords = [x, y]
        self.obstacles.append(coords)

    # Turns robot left or right depending on the instruction argument
    def rotate(self, instruction):

        if instruction not in ('LEFT', 'RIGHT'):
            print("Invalid rotate instruction. Please tell the robot to rotate either LEFT or RIGHT")

        if instruction is 'LEFT' and self.direction_index is 0:
            self.direction_index = len(self.direction) - 1
        elif instruction is 'LEFT' and self.direction_index is not 0:
            self.direction_index -= 1
        elif instruction is 'RIGHT' and self.direction_index is len(self.direction) - 1:
            self.direction_index = 0
        elif instruction is 'RIGHT' and self.direction_index is not len(self.direction) - 1:
            self.direction_index += 1
        self.f = self.direction[self.direction_index]

    # Moves robot one unit in the direction it is facing
    def move(self):
        current_position = [self.x, self.y]
        # invalid moves/corner
        if self.x == self.y == self.min_pos and (self.f == 'WEST' or self.f == 'SOUTH'):
            print("Robot is in the south west corner facing " + self.f + " and can no longer move forward")
            return
        if self.x == self.y == self.max_pos and (self.f == 'EAST' or self.f == 'NORTH'):
            print("Robot is in the north east corner facing " + self.f + " and can no longer move forward")
            return
        if self.x == self.min_pos and self.y == self.max_pos and (self.f == 'WEST' or self.f == 'NORTH'):
            print("Robot is in the north west corner facing " + self.f + " and can no longer move forward")
            return
        if self.x == self.max_pos and self.y == self.min_pos and (self.f == 'WEST' or self.f == 'SOUTH'):
            print("Robot is in the south west corner facing " + self.f + " and can no longer move forward")
            return

        # invalid moves/side
        if self.x == self.min_pos and self.f == 'WEST':
            print("Robot is on the west side of the grid facing " + self.f + " and can no longer move forward")
            return
        if self.x == self.max_pos and self.f == 'EAST':
            print("Robot is on the east side of the grid facing " + self.f + " and can no longer move forward")
            return
        if self.y == self.min_pos and self.f == 'SOUTH':
            print("Robot is on the south side of the grid facing " + self.f + " and can no longer move forward")
            return
        if self.y == self.max_pos and self.f == 'NORTH':
            print("Robot is on the north side of the grid facing " + self.f + " and can no longer move forward")
            return

        # valid moves
        if self.f == 'NORTH':
            self.y += 1
        elif self.f == 'EAST':
            self.x += 1
        elif self.f == 'SOUTH':
            self.y -= 1
        elif self.f == 'WEST':
            self.x -= 1

        # check for obstacles
        if [self.x, self.y] in self.obstacles:
            print("Cell is obstructed, robot did not move")
            self.x = current_position[0]
            self.y = current_position[1]

    def clear_obstacles(self):
        self.obstacles = []

    def report_placed(self):
        return self.place_flag

    # Reports the current location/coordinates of the robot
    def report(self):
        report_string = str(self.x) + "," + str(self.y) + "," + self.f
        return report_string

    def report_obstacles(self):
        print(self.obstacles)
        return self.obstacles
