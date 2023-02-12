
import struct
import serial
from PyQt5.QtCore import QObject, QThread, pyqtSignal, Qt
from multiprocessing import Process, Pipe



class SensorBoard(QObject):
    def __init__(self, name, com_port, baude_rate, num_sensors):
        super().__init__()
        self.name = str(name)
        self.com_port = str(com_port)
        self.baude_rate = int(baude_rate)
        self.num_sensors = num_sensors
        self.Serial_connection = serial.Serial(self.com_port, self.baude_rate, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
        self.data_pipe = object



    def add_pipe(self, data_pipe):
        self.data_pipe = data_pipe

    def set_serial_input_order(self, serial_input_order):
        self.serial_input_order = serial_input_order

    def get_serial_input_order(self): return self.serial_input_order

    def print_properties(self):
        print(f"Name: {self.name}")
        print(f"COM-Port:  {self.com_port}")
        print(f"Bauderate: {self.baude_rate}")
        print(f"Number of Sensors enabled: {self.num_sensors}")  # TODO: Change to List of Sensor names

    def read_serial_data(self):  # TODO: Check for order of incoming values first
        """reads serial data from an arduino byte stream, each sensor sends it 4Byte Float after another
           performs task only ones
           returns array of length num_sensors as type(float)"""
        while True:
            signal = []
            read = True
            while read:
                signal.append(self.Serial_connection.read(4))  # reads four bytes (= float) from the serial stream, add each value to signal
                if signal.__len__() >= self.num_sensors:  # waits until each package (= each Sensor) is read

                    # loops over all bytes in signal and converts them into float -> returns vector
                    sensor_values = [struct.unpack("f", bytes(signal[x]))[0] for x in range(0, self.num_sensors, 1)]
                    signal.clear()  # clears signal vector after converting
                    read = False  # stop reading from serial Port, until called again
                    self.data_pipe.send(sensor_values)   # returns Value vector of size number_of_packages type float




