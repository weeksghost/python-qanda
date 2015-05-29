import serial
from time import sleep
from time import strftime


device_a = serial.Serial(
            port='/dev/cu.Bluetooth-Incoming-Port',
            baudrate=9600,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS,
            timeout=3
)

device_b = serial.Serial(
            port='/dev/cu.Bluetooth-Incoming-Port',
            baudrate=9600,
            parity=serial.PARITY_ODD,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.SEVENBITS,
            timeout=3
)


def test_connect():

    device_a.close()
    device_a.open()

    # TODO
    # 2) Add asserts to verify reads + writes
    # 3) Wrap up in a function
    # 4) Use datetime for micro/miliseconds

    if device_a.isOpen():
        for _ in xrange(1):
            try:
                port = device_a.port
                device_a.flushInput()
                device_a.flushOutput()
                #device_a.write('Hello world 1') Represents acutal write
                print('Dev A: [{}] {}'.format(
                    strftime('%H:%M:%S'), 'Chan 0 Send_msg cmd is issued')
                )
                sleep(.5)
                print('Dev A: [{}] {}'.format(
                    strftime('%H:%M:%S'), 'message sent: Hello world 1')
                )
                #response = device_a.readline() Represents acutal read
                print('Dev B: [{}] {}'.format(
                    strftime('%H:%M:%S'), 'Chan 0 Received msg: {}'.format(
                        'Hello World 1'))
                )
                print('Dev A: [{}] {}'.format(
                    strftime('%H:%M:%S'), 'Chan 1 Send_msg cmd is issued')
                )
                sleep(.5)
                print('Dev A: [{}] {}'.format(
                    strftime('%H:%M:%S'), 'message sent: Hello world 2')
                )
                #response = device_a.readline() Represents acutal read
                print('Dev B: [{}] {}'.format(
                    strftime('%H:%M:%S'), 'Chan 1 Received msg: {}'.format(
                        'Hello World 2'))
                )
            except serial.SerialException:
                print('Could not connect to: {}'.format(port))
        device_a.close()

test_connect()
