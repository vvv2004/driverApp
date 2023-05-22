import math
import time

from adafruit_servokit import ServoKit

initial_values = {
    0: 100,
    1: 110,
    4: 110
}


class Robot:

    def __init__(self, speed):
        self.kit = ServoKit(channels=16)
        self.motor_indexes = [0, 1, 4, 5, 8, 11]
        self._speed = speed

    def startup_procedure(self):
        self._take_robot_to_initial_position()

    def _take_robot_to_initial_position(self):
        speed = self._speed

        self.kit.servo[0].angle = initial_values[0]
        self.kit.servo[1].angle = initial_values[1]
        self.kit.servo[4].angle = initial_values[4]

        self._take_robot_to_working_position()

    def _take_robot_to_working_position(self):
        speed = self._speed

        self.move_motor(0, 30, speed)
        self.move_motor(1, 180, speed)
        self.move_motor(4, 180, speed)

    def move_motor(self, motor_index, target_angle, speed):
        # if the index is not occupied with servo on the board
        if not self.motor_indexes.__contains__(motor_index):
            raise Exception("Invalid index")
        # if there is a motor on the given index
        else:
            motor = self.kit.servo[motor_index]
            motor_angle = motor.angle  # get the angle

            # move gradually until the desired angle is reached
            while math.ceil(motor_angle) != target_angle:
                if motor_angle < target_angle:
                    motor_angle += speed
                elif motor_angle > target_angle:
                    motor_angle -= speed

                time.sleep(.1)
                motor.angle = motor_angle
