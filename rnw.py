import struct

from robot import Robot

def get_displacement_data_test():
    output_array = []

    for i in range(6):
        if i == 2:
            output_array.append(85.0)
        else:
            output_array.append(0.0)

    return output_array

class Reader:

    def __init__(self, file_destination):
        self._file_destination = file_destination
        # self.robot = robot

    def read_from_file(self):
        output = []

        with open(self._file_destination, 'rb') as file:
            # read byte by byte
            num_of_doubles = 6
            try:
                byte_array = file.read(num_of_doubles * 8)
                doubles = struct.unpack('>' + 'd' * num_of_doubles, byte_array)

                output = doubles
            except Exception:
                print("Java is writing0")

        return output


class Writer:
    def __init__(self, file_destination):
        self._file_destination = file_destination

    def write_to_file(self, data: Robot):

        with open(self._file_destination, "wb") as file:
            try:
                for double in data.get_displacement_data():
                    binary_data = struct.pack('>' + 'd', double)
                    file.write(binary_data)

            except Exception:
                print('Java is writing1')

    # def write_to_file_test(self):
    #     with open(self._file_destination, "wb") as file:
    #         try:
    #             for double in get_displacement_data_test():
    #                 binary_data = struct.pack('>' + 'd', double)
    #                 file.write(binary_data)
    #
    #         except Exception:
    #             print('Java is writing')