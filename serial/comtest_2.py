from time import sleep
from time import strftime


def exec_cmd(device, cmd):
    for _ in xrange(1, 101):
        try:

            # Initialize device(s)
            device.close()
            device.open()
            device.flushInput()
            device.flushOutput()
            device.flushInput()
            device.flushOutput()

            # Get port handle
            port = device.port

            # Assign channels to tuples as mock code for referencing channels
            channels = 0,1

            # Send command to device
            send = device.write(cmd)

            # Mock code for distinguishing channel with subsequent optput
            # based on input
            if 0 in send:
                print('Dev A: [{}] Chan 0 Send_msg cmd is issued'.format(
                        strftime('%H:%M:%S')))

                # Give recieving device time to process
                sleep(1)

                print('Dev A: [{}] message sent: Hello world 1'.format(
                        strftime('%H:%M:%S')))

            # If command not through channel 0
            print('Dev A: [{}] Chan 1 Send_msg cmd is issued'.format(
                    strftime('%H:%M:%S')))
            sleep(1)

            print('Dev A: [{}] message sent: Hello world 2'.format(
                    strftime('%H:%M:%S')))

            # Mock code for recieving device
            recv = device.readline()

            if recv != send:
                print('')

            if send in channels[0]:
                print('Dev B: [{}] Chan 0 Received msg: Hello world 1'.format(
                    strftime('%H:%M:%S')))
            print('Dev B: [{}] Chan 1 Received msg: Hello world 2'.format(
                strftime('%H:%M:%S')))
        except IOError:
            print('Could not connect to: {}'.format(port))
