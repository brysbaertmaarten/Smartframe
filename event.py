import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

buttons = [21,20,16,12]

def actie(pin):
    index = buttons.index(pin)
    print("Ingedrukt: " + str(index + 1))

for button in buttons:
    GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)
    GPIO.add_event_detect(button, GPIO.RISING, actie, 400)

try:
    while True:
        time.sleep(60)

except KeyboardInterrupt:
    print("Einde")

GPIO.cleanup()