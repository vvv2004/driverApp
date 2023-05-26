import struct


class Reader:

    def __init__(self, file_destination):
        self._file_destination = file_destination

    def read_from_file(self):
        output = []

        with open(self._file_destination, 'rb') as file:
            # read byte by byte
            num_of_doubles = 6
            try:
                byte_array = file.read(num_of_doubles * 8)
                doubles = struct.unpack('>' + 'd' * num_of_doubles, byte_array)

                byte_array = file.read(2)
                booleans = struct.unpack('?' * 2, byte_array)

                output = doubles
                output += booleans
            except Exception:
                print("Java is writing")

        return output


class Writer:
    def __init__(self, file_destination):
        self._file_destination = file_destination
