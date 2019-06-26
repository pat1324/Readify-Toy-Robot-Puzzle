import unittest
import ToyRobot


class TestRobot(unittest.TestCase):

    # TESTING USING EXAMPLES SUPPLIED

    def test_example_a(self):
        robot = ToyRobot.Robot()
        robot.place(0,0,'NORTH')
        robot.move()
        expected = "0,1,NORTH"
        self.assertEqual(robot.report(), expected)

    def test_example_b(self):
        robot = ToyRobot.Robot()
        robot.place(0,0,'NORTH')
        robot.rotate('LEFT')
        expected = "0,0,WEST"
        self.assertEqual(robot.report(), expected)

    def test_example_c(self):
        robot = ToyRobot.Robot()
        robot.place(1,2,'EAST')
        robot.move()
        robot.move()
        robot.rotate('LEFT')
        robot.move()
        expected = "3,3,NORTH"
        self.assertEqual(robot.report(), expected)

    # TESTING PLACE COMMAND

    def test_initial_place(self):
        robot = ToyRobot.Robot()
        robot.place(2,2,'NORTH')
        expected = "2,2,NORTH"
        self.assertEqual(robot.report(), expected)

    def test_non_initial_place(self):
        robot = ToyRobot.Robot()
        robot.place(4, 4, 'SOUTH')
        robot.place(0, 0, 'EAST')
        expected = "0,0,EAST"
        self.assertEqual(robot.report(), expected)

    def test_invalid_place(self):
        robot = ToyRobot.Robot()
        robot.place(4, 4, 'SOUTH')
        robot.place(10, 10, 'NORTH')
        expected = "4,4,SOUTH"
        self.assertEqual(robot.report(), expected)

    # TESTING VALID MOVES

    def test_move_north(self):
        robot = ToyRobot.Robot()
        robot.place(0, 0, 'NORTH')
        robot.move()
        expected = "0,1,NORTH"
        self.assertEqual(robot.report(), expected)

    def test_move_south(self):
        robot = ToyRobot.Robot()
        robot.place(1, 1, 'SOUTH')
        robot.move()
        expected = "1,0,SOUTH"
        self.assertEqual(robot.report(), expected)

    def test_move_east(self):
        robot = ToyRobot.Robot()
        robot.place(0, 0, 'EAST')
        robot.move()
        expected = "1,0,EAST"
        self.assertEqual(robot.report(), expected)

    def test_move_west(self):
        robot = ToyRobot.Robot()
        robot.place(2, 0, 'WEST')
        robot.move()
        expected = "1,0,WEST"
        self.assertEqual(robot.report(), expected)

    # TESTING INVALID MOVES FROM SIDES OF GRID

    def test_move_north_when_at_top_of_grid(self):
        robot = ToyRobot.Robot()
        robot.place(3, 4, 'NORTH')
        robot.move()
        expected = "3,4,NORTH"
        self.assertEqual(robot.report(), expected)

    def test_move_south_when_at_bottom_of_grid(self):
        robot = ToyRobot.Robot()
        robot.place(1, 0, 'SOUTH')
        robot.move()
        expected = "1,0,SOUTH"
        self.assertEqual(robot.report(), expected)

    def test_move_west_when_at_left_of_grid(self):
        robot = ToyRobot.Robot()
        robot.place(0, 3, 'WEST')
        robot.move()
        expected = "0,3,WEST"
        self.assertEqual(robot.report(), expected)

    def test_move_east_when_at_right_of_grid(self):
        robot = ToyRobot.Robot()
        robot.place(4, 3, 'EAST')
        robot.move()
        expected = "4,3,EAST"
        self.assertEqual(robot.report(), expected)

    # TESTING INVALID MOVES FROM CORNERS OF GRID

    def test_move_north_when_at_north_west_of_grid(self):
        robot = ToyRobot.Robot()
        robot.place(0, 4, 'NORTH')
        robot.move()
        expected = "0,4,NORTH"
        self.assertEqual(robot.report(), expected)

    def test_move_west_when_at_north_west_of_grid(self):
        robot = ToyRobot.Robot()
        robot.place(0, 4, 'WEST')
        robot.move()
        expected = "0,4,WEST"
        self.assertEqual(robot.report(), expected)

    def test_move_west_when_at_south_west_of_grid(self):
        robot = ToyRobot.Robot()
        robot.place(0, 0, 'WEST')
        robot.move()
        expected = "0,0,WEST"
        self.assertEqual(robot.report(), expected)

    def test_move_south_when_at_south_west_of_grid(self):
        robot = ToyRobot.Robot()
        robot.place(0, 0, 'SOUTH')
        robot.move()
        expected = "0,0,SOUTH"
        self.assertEqual(robot.report(), expected)

    def test_move_south_when_at_south_east_of_grid(self):
        robot = ToyRobot.Robot()
        robot.place(4, 0, 'SOUTH')
        robot.move()
        expected = "4,0,SOUTH"
        self.assertEqual(robot.report(), expected)

    def test_move_east_when_at_south_east_of_grid(self):
        robot = ToyRobot.Robot()
        robot.place(4, 0, 'EAST')
        robot.move()
        expected = "4,0,EAST"
        self.assertEqual(robot.report(), expected)

    def test_move_east_when_at_north_east_of_grid(self):
        robot = ToyRobot.Robot()
        robot.place(4, 4, 'EAST')
        robot.move()
        expected = "4,4,EAST"
        self.assertEqual(robot.report(), expected)

    def test_move_north_when_at_north_east_of_grid(self):
        robot = ToyRobot.Robot()
        robot.place(4, 4, 'NORTH')
        robot.move()
        expected = "4,4,NORTH"
        self.assertEqual(robot.report(), expected)

    # TESTING ROTATING LEFT AND RIGHT

    def test_rotate_left_from_north(self):
        robot = ToyRobot.Robot()
        robot.place(2, 0, 'NORTH')
        robot.rotate('LEFT')
        expected = "2,0,WEST"
        self.assertEqual(robot.report(), expected)

    def test_rotate_right_from_north(self):
        robot = ToyRobot.Robot()
        robot.place(2, 0, 'NORTH')
        robot.rotate('RIGHT')
        expected = "2,0,EAST"
        self.assertEqual(robot.report(), expected)

    def test_rotate_left_from_west(self):
        robot = ToyRobot.Robot()
        robot.place(2, 0, 'WEST')
        robot.rotate('LEFT')
        expected = "2,0,SOUTH"
        self.assertEqual(robot.report(), expected)

    def test_rotate_right_from_west(self):
        robot = ToyRobot.Robot()
        robot.place(2, 0, 'WEST')
        robot.rotate('RIGHT')
        expected = "2,0,NORTH"
        self.assertEqual(robot.report(), expected)


if __name__ == "__main__":
    unittest.main()
