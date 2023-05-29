from rnw import *
from robot import Robot

file_destination = '/home/robot/ControllApp/control.arm'
reader = Reader(file_destination)

robot = Robot(0.045, file_destination)
robot.reset_motors()
robot.startup_procedure()


writer = Writer(file_destination)
writer.write_to_file(robot)


while True:
    data = reader.read_from_file()

    for i in range(1, 6):
        robot.move_joint(i, data[i])

