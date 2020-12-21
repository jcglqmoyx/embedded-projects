import RPi.GPIO
import time

RPi.GPIO.setwarnings(False)

RPi.GPIO.setmode(RPi.GPIO.BOARD)

RPi.GPIO.setup(11, RPi.GPIO.OUT)
RPi.GPIO.setup(12, RPi.GPIO.OUT)
RPi.GPIO.setup(13, RPi.GPIO.OUT)
RPi.GPIO.setup(15, RPi.GPIO.OUT)
RPi.GPIO.setup(26, RPi.GPIO.OUT)
RPi.GPIO.setup(29, RPi.GPIO.OUT)
RPi.GPIO.setup(31, RPi.GPIO.OUT)
RPi.GPIO.setup(33, RPi.GPIO.OUT)
RPi.GPIO.setup(35, RPi.GPIO.OUT)
RPi.GPIO.setup(37, RPi.GPIO.OUT)

i = 1
while True:
    RPi.GPIO.output(11, 1)
    time.sleep(0.2)
    RPi.GPIO.output(11, 0)

    RPi.GPIO.output(12, 1)
    time.sleep(0.2)
    RPi.GPIO.output(12, 0)

    RPi.GPIO.output(13, 1)
    time.sleep(0.2)
    RPi.GPIO.output(13, 0)

    RPi.GPIO.output(15, 1)
    time.sleep(0.2)
    RPi.GPIO.output(15, 0)

    RPi.GPIO.output(29, 1)
    time.sleep(0.2)
    RPi.GPIO.output(29, 0)

    RPi.GPIO.output(15, 1)
    time.sleep(0.2)
    RPi.GPIO.output(15, 0)
    RPi.GPIO.output(15, 1)
    time.sleep(0.2)
    RPi.GPIO.output(15, 0)
    RPi.GPIO.output(15, 1)
    time.sleep(0.2)
    RPi.GPIO.output(15, 0)
    RPi.GPIO.output(15, 1)
    time.sleep(0.2)
    RPi.GPIO.output(15, 0)
    i += 1
    if i == 10:
        break

RPi.GPIO.cleanup()


import datetime

current_date = datetime.datetime.now()
hour = current_date.hour
minute = current_date.minute
print(current_date)
