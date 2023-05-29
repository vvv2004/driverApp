import math
import time
# from main import file_destination

from adafruit_servokit import ServoKit

initial_values = {
    0: 90,
    1: 110,
    4: 110,
    5: 110,
    8: 180,
    11: 20
}

maxb_values = {
    0: 25,
    1: None,
    4: 180,
    5: 25,
    8: 180,
    11: 0
}

maxf_values = {
    0: 155,
    1: None,
    4: 10,
    5: 180,
    8: 23,
    11: 120
}

constraints = {
    0: None,
    1: None,
    4: 85.0

}

correlation_bma = [
    None,
    0,
    4,
    5,
    11,
    8
]


class Robot:

    def __init__(self, speed, file_destination):
        self.kit = ServoKit(channels=16)
        self.motor_indexes = [0, 1, 4, 5, 8, 11]
        self._speed = speed
        self._file_destination = file_destination

    # def workflow(self):
    #     reader = Reader(self._file_destination)
    #     print(reader.read_from_file())

    def startup_procedure(self):
        self._take_robot_to_initial_position()

    def _take_robot_to_initial_position(self):
        speed = self._speed

        # self.kit.servo[0].angle = initial_values[0]
        # self.kit.servo[1].angle = initial_values[1]
        self.kit.servo[4].angle = initial_values[4]

        time.sleep(3)

        self._take_robot_to_working_position()

    def move_joint(self, joint_to_move, new_value):
        if joint_to_move != 1:
            self.move_motor(correlation_bma[joint_to_move], new_value, self._speed)
        else:
            #to do synchronising
            return 0

    def reset_motors(self):
        self.kit.servo[0].angle = None
        self.kit.servo[1].angle = None
        self.kit.servo[4].angle = None

    def _take_robot_to_working_position(self):
        speed = self._speed

        # self.move_motor(0, 30, speed)
        # self.move_motor(1, 180, speed)
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

                # time.sleep(.1)
                motor.angle = motor_angle

    def get_data(self):
        output_array = []

        for i in range(6):
            output_array.append(self.kit.servo[correlation_bma[i]].angle)

        return output_array

    def get_displacement_data(self):
        data_as_angles = self.get_data()
        output_array = []

        for i in range(6):
            midpoint = constraints[correlation_bma[i]]

            output_array.append(data_as_angles[i] - midpoint)

        return output_array
