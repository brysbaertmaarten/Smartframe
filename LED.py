import RPi.GPIO as GPIO
import time

class LED:

    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.__pin = pin

    def led_knipperen(self):
        GPIO.output(self.__pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(self.__pin, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(self.__pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(self.__pin, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(self.__pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(self.__pin, GPIO.LOW)

    def led_aan(self):
        GPIO.output(self.__pin, GPIO.HIGH)