import unittest
import ToyRobot


class TestRobot(unittest.TestCase):

    def test_place_without_direction_and_not_placed(self):
        robot = ToyRobot.Robot()
        robot.place(5,5)
        self.assertEqual(robot.report_placed(), False)

    def test_place_without_direction_and_already_placed(self):
        robot = ToyRobot.Robot()
        robot.place(3,3,'NORTH')
        robot.place(5,5)
        expected = "5,5,NORTH"
        self.assertEqual(expected, robot.report())







if __name__ == "__main__":
    unittest.main()
