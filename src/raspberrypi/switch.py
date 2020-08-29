import time

import RPi.GPIO

red = 11
green = 12

button1 = 13
button2 = 14

RPi.GPIO.setwarnings(False)

RPi.GPIO.setmode(RPi.GPIO.BOARD)

RPi.GPIO.setup(red, RPi.GPIO.OUT)
RPi.GPIO.setup(green, RPi.GPIO.OUT)

RPi.GPIO.setup(button1, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
RPi.GPIO.setup(button2, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
try:
    RPi.GPIO.output(red, 1)
    RPi.GPIO.output(green, 1)

    while True:
        time.sleep(0.5)
        if RPi.GPIO.input(button1) == 0:
            RPi.GPIO.output(red, 1)
        else:
            RPi.GPIO.output(red, 0)

        if RPi.GPIO.input(button2) == 0:
            RPi.GPIO.output(green, 1)
        else:
            RPi.GPIO.output(green, 0)
except KeyboardInterrupt:
    pass
