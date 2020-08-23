import RPi.GPIO
import time

RPi.GPIO.setwarnings(False)

RPi.GPIO.setmode(RPi.GPIO.BOARD)

RPi.GPIO.setup(11, RPi.GPIO.OUT)
RPi.GPIO.setup(12, RPi.GPIO.OUT)
RPi.GPIO.setup(13, RPi.GPIO.OUT)

i = 1
while True:
    RPi.GPIO.output(11, 1)
    print('red\n')
    time.sleep(2)
    RPi.GPIO.output(11, 0)

    RPi.GPIO.output(12, 1)
    print('green\n')
    time.sleep(2)
    RPi.GPIO.output(12, 0)

    RPi.GPIO.output(13, 1)
    print('blue\n')
    time.sleep(2)
    RPi.GPIO.output(13, 0)

    i += 1
    if i == 5:
        break

RPi.GPIO.cleanup()
