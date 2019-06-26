class Robot:

    direction = ['NORTH', 'EAST', 'SOUTH', 'WEST']
    min_pos = 0
    max_pos = 4
    direction_index = None

    def __init__(self, x=None, y=None, f=None):
        self.x = x
        self.y = y
        self.f = f

    # Places robot on the grid. The use of regex to enforce valid input means that invalid coordinates cannot be passed
    # into the method. The invalid input guards are included in case of future modification.
    def place(self, x, y, f):
        if x < self.min_pos or x > self.max_pos:
            print("Invalid coordinates. Please enter x and y values between 0 and 4 inclusive")
            return
        if y < self.min_pos or y > self.max_pos:
            print("Invalid coordinates. Please enter x and y values between 0 and 4 inclusive")
            return
        if f not in self.direction:
            print("Invalid direction. Please enter a direction of NORTH, SOUTH, EAST OR WEST")
            return
        self.x = x
        self.y = y
        self.f = f
        self.direction_index = self.direction.index(self.f)  # tracks direction in the direction list

    # Turns robot left or right depending on the instruction argument
    def rotate(self, instruction):

        if instruction not in ('LEFT', 'RIGHT'):
            print("Invalid rotate instruction. Please tell PacMan to rotate either LEFT or RIGHT")

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

    # Reports the current location/coordinates of the robot
    def report(self):
        report_string = str(self.x) + "," + str(self.y) + "," + self.f
        return report_string
