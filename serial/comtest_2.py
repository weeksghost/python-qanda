import serial
from time import sleep


COMMAND1 = 'Hello World 1'

device_a = serial.Serial(
            port='/dev/cu.Bluetooth-Incoming-Port',
            baudrate=9600,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS,
            timeout=0
)

device_b = serial.Serial(
            port='/dev/cu.Bluetooth-Incoming-Port',
            baudrate=9600,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS,
            timeout=3
)

#def test_connect(device, cmd):
#    pass

device_a.close()
device_a.open()

# TODO
# 1) Create loop of 100 writes + reads
# 2) Add asserts to verify reads + writes
# 3) Figure out how to code this so ports are talking to each other
# 4) Wrap up in a function

if device_a.isOpen():
    try:
        device_a.flushInput()
        device_a.flushOutput()
        device_a.write(COMMAND1+'\r\n')
        print('Sending {} to Port'.format(COMMAND1))
        sleep(1)
        lines = 0
        while True:
            response = device_a.readline()
            print('Port is reading {}'.format(COMMAND1))
            lines += 1
            if lines >= 1:
                break
        device_a.close()
    except serial.SerialException:
        print('error')
