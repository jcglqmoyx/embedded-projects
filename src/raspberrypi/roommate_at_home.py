import datetime
import os
import time

import RPi.GPIO

while True:
    time.sleep(1)
    ip = '192.168.1.2'
    back_info = os.system('ping -c 1 -w 1 %s' % ip)
    if back_info:
        print('not at home')
    else:
        print('at home')
        time_when_his_phone_connected_to_wifi = str(datetime.datetime.now().hour) + ':' + str(
            datetime.datetime.now().minute)
        print(time_when_his_phone_connected_to_wifi)
        file = open('time.txt', 'w')
        file.write(time_when_his_phone_connected_to_wifi)
        file.close()
        RPi.GPIO.setwarnings(False)

        RPi.GPIO.setmode(RPi.GPIO.BOARD)

        RPi.GPIO.setup(11, RPi.GPIO.OUT)
        RPi.GPIO.setup(12, RPi.GPIO.OUT)
        RPi.GPIO.setup(13, RPi.GPIO.OUT)

        i = 1
        while True:
            RPi.GPIO.output(11, 1)
            RPi.GPIO.output(12, 1)
            RPi.GPIO.output(13, 1)

            time.sleep(2)

            RPi.GPIO.output(11, 0)
            RPi.GPIO.output(12, 0)
            RPi.GPIO.output(13, 0)

            i += 1
            if i == 5:
                break

    RPi.GPIO.cleanup()
