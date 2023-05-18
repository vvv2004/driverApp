from rnw import Reader
from robot import Robot

file_destination = 'D:\\Development\\IntelliJ\\ControllApp\\control.arm'
reader = Reader(file_destination)

# while True:
#     print(reader.read_from_file())

robot = Robot(0.5)
robot.startup_procedure()

print("This is a test")
