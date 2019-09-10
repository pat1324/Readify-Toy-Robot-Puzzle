import unittest
import ToyRobot



class TestAvoid(unittest.TestCase):

    def test_avoid_two_cells(self):
        robot = ToyRobot.Robot()
        robot.avoid(4, 4)
        robot.avoid(2, 2)
        expected = [[4,4], [2,2]]
        self.assertEqual(expected, robot.report_obstacles())

    def test_clear_obstacles(self):
        robot = ToyRobot.Robot()
        robot.avoid(3,3)
        robot.avoid(2,2)
        robot.clear_obstacles()
        self.assertEqual(robot.report_obstacles(), [])

    def test_avoid_place(self):
        robot = ToyRobot.Robot()
        robot.clear_obstacles()
        robot.avoid(4, 4)
        robot.place(4, 4, 'NORTH')
        self.assertEqual(robot.place_flag, False)

    def test_success_place(self):
        robot = ToyRobot.Robot()
        robot.clear_obstacles()
        robot.avoid(3,3)
        robot.place(2,2,'NORTH')
        self.assertEqual(robot.place_flag, True)

    def test_avoid_same_cell(self):
        robot = ToyRobot.Robot()
        robot.clear_obstacles()
        robot.avoid(3,3)
        robot.avoid(3,3)
        expected = [[3,3]]#avoid duplicates
        self.assertEqual(expected, robot.report_obstacles())

    # MOVEMENT

    def test_avoid_obstacle(self):
        robot = ToyRobot.Robot()
        robot.clear_obstacles()
        robot.avoid(3,3)
        robot.place(3,2,'NORTH')
        robot.move()
        expected = "3,2,NORTH"
        self.assertEqual(expected, robot.report())


if __name__ == "__main__":
    unittest.main()
