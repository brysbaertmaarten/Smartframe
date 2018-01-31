import RPi.GPIO as GPIO
import time

class Buzzer:

    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.__pin = pin
        self.__p = GPIO.PWM(pin, 261)

    def lawaai_buzzer_add_contact(self):
        self.__p.start(50)
        time.sleep(0.2)
        self.__p.stop()
        time.sleep(0.2)
        self.__p.start(50)
        time.sleep(0.2)
        self.__p.stop()
        time.sleep(0.2)
        self.__p.start(50)
        time.sleep(0.2)
        self.__p.stop()
        time.sleep(0.2)

    def lawaai_buzzer_add_frame(self):
        self.__p.start(50)
        time.sleep(0.2)
        self.__p.stop()
        time.sleep(0.2)
        self.__p.start(50)
        time.sleep(0.2)
        self.__p.stop()
        time.sleep(0.2)

    def lawaai_buzzer_druk_knop(self):
        self.__p.start(50)
        time.sleep(0.2)
        self.__p.stop()
        time.sleep(0.2)