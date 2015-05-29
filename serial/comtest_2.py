import serial
from time import sleep
from time import gmtime
from time import strftime


COMMAND1 = 'Hello World 1'

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
    # 1) Create loop of 100 writes + reads
    # 2) Add asserts to verify reads + writes
    # 3) Wrap up in a function
    # 4) Use datetime for micro/miliseconds

    if device_a.isOpen():
        try:
            port = device_a.port
            device_a.flushInput()
            device_a.flushOutput()

            #device_a.write('Chan 1 Send_msg  Hello world 2')

            device_a.write('Hello world 1')

            print('Dev A: [{}] {}'.format(
                strftime('%H:%M:%S'), 'Chan 0 Send_msg cmd is issued')
            )

            sleep(.5)

            print('Dev A: [{}] {}'.format(
                strftime('%H:%M:%S'), 'message sent: Hello world 1')
            )

            lines = 0
            while True:
                response = device_a.readline()
                print('Dev B: [{}] {}'.format(
                    strftime('%H:%M:%S'), 'Chan 0 Received msg: {}'.format(
                        'Hello World 1'))
                )
                lines += 1
                if lines >= 1:
                    break
            device_a.close()
        except serial.SerialException:
            print('error')

test_connect()
