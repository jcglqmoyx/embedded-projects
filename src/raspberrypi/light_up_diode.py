import datetime
import time

import RPi.GPIO

current_date = datetime.datetime.now()
hour = current_date.hour
hour = hour % 12
minute = current_date.minute
print(current_date)

RPi.GPIO.setwarnings(False)
RPi.GPIO.setmode(RPi.GPIO.BOARD)

RPi.GPIO.setup(11, RPi.GPIO.OUT)
RPi.GPIO.setup(12, RPi.GPIO.OUT)
RPi.GPIO.setup(13, RPi.GPIO.OUT)
RPi.GPIO.setup(15, RPi.GPIO.OUT)
RPi.GPIO.setup(29, RPi.GPIO.OUT)
RPi.GPIO.setup(31, RPi.GPIO.OUT)
RPi.GPIO.setup(33, RPi.GPIO.OUT)
RPi.GPIO.setup(35, RPi.GPIO.OUT)
RPi.GPIO.setup(36, RPi.GPIO.OUT)
RPi.GPIO.setup(37, RPi.GPIO.OUT)

i = 1

h = hour
m = minute
while True:
    hour = h
    minute = m
    if hour >= 8:
        hour -= 8
        RPi.GPIO.output(11, 1)
    else:
        RPi.GPIO.output(11, 0)

    if hour >= 4:
        hour -= 4
        RPi.GPIO.output(12, 1)
    else:
        RPi.GPIO.output(12, 0)

    if hour >= 2:
        hour -= 2
        RPi.GPIO.output(13, 1)
    else:
        RPi.GPIO.output(13, 0)

    if hour >= 1:
        hour -= 1
        RPi.GPIO.output(15, 1)
    else:
        RPi.GPIO.output(15, 0)

    if minute >= 32:
        minute -= 32
        RPi.GPIO.output(29, 1)
    else:
        RPi.GPIO.output(29, 0)

    if minute >= 16:
        minute -= 16
        RPi.GPIO.output(31, 1)
    else:
        RPi.GPIO.output(31, 0)

    if minute >= 8:
        minute -= 8
        RPi.GPIO.output(33, 1)
    else:
        RPi.GPIO.output(33, 0)

    if minute >= 4:
        minute -= 4
        RPi.GPIO.output(35, 1)
    else:
        RPi.GPIO.output(35, 0)

    if minute >= 2:
        minute -= 2
        RPi.GPIO.output(36, 1)
    else:
        RPi.GPIO.output(36, 0)

    if minute >= 1:
        minute -= 1
        RPi.GPIO.output(37, 1)
    else:
        RPi.GPIO.output(37, 0)

    time.sleep(0.1)
    i += 1
    #if i == 1000:
    #    break

RPi.GPIO.cleanup()
