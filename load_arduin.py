# Ref: https://github.com/WaveShapePlay/ArduinoPyserialComConnect/blob/master/findArduino.py

import serial.tools.list_ports

speed_port = [str(v) for v in [9600, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200]]

def get_ports():
    # Function to return arduins ports
    port_arduin = serial.tools.list_ports.comports()
    return port_arduin

def find_arduin_port(found_ports):
    # Function to Found ports in arduin
    com_port = None
    n_ports = len(found_ports)

    for idx in range(0, n_ports):
        port_ = found_ports[i]
        str_port = str(port_)

        if 'Arduino' in str_port:
            split_port = str_port.split(' ')
            com_port = (split_port[0])

    return com_port

port_returned = get_ports()

connect_to_port = find_arduin_port(port_returned)

if connect_to_port != None:
    serial_port_arduin = serial.Serial(connect_to_port, baudrate=speed_port[0], timeout=1)
    print('Connected to port ' + connect_to_port)
else:
    print("Problem to connect port!\nMake sure the arduino is connected!\n")