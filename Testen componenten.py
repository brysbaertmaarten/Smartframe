import RPi.GPIO as GPIO
import time
from LED import LED
from Knop import Knop
from Buzzer import Buzzer

GPIO.setmode(GPIO.BCM)

# knop1_ingedrukt = 1
# knop2_ingedrukt = 1
# knop3_ingedrukt = 1
# knop4_ingedrukt = 1

led = LED(25)
buzzer = Buzzer(23)
buttons = [21,20,16,12]

# GPIO.setup(led,GPIO.OUT)
# GPIO.setup(buzzer,GPIO.OUT)

# p = GPIO.PWM(buzzer,261)

knop1 = Knop(buttons[0])
knop2 = Knop(buttons[1])
knop3 = Knop(buttons[2])
knop4 = Knop(buttons[3])
    # GPIO.add_event_detect(button, GPIO.RISING, actie, 400)

# def led_knipperen():
#     GPIO.output(led,GPIO.HIGH)
#     time.sleep(0.5)
#     GPIO.output(led, GPIO.LOW)
#     time.sleep(0.5)
#     GPIO.output(led,GPIO.HIGH)
#     time.sleep(0.5)
#     GPIO.output(led, GPIO.LOW)

# def actie(pin):
#     index = buttons.index(pin)
#     print("Knop " + str(index + 1) + " is ingedrukt!")
#
# def lawaai_buzzer():
#     p.start(50)
#     time.sleep(0.5)
#     p.stop()
#     time.sleep(0.5)
#     p.start(50)
#     time.sleep(0.5)
#     p.stop()
#     time.sleep(0.5)
#     p.start(50)
#     time.sleep(0.5)
#     p.stop()
#     time.sleep(0.5)

try:
    while True:
        # led.led_knipperen()
        knop1.knop_ingedrukt()
        knop2.knop_ingedrukt()
        knop3.knop_ingedrukt()
        knop4.knop_ingedrukt()
        # led_knipperen()
        # knop1 = GPIO.input(buttons[0])
        # print(knop1)
        # if (not knop1 and (knop1_ingedrukt != knop1)):
        #     actie(21)
        #     knop1_ingedrukt = 0
        # knop2 = GPIO.input(buttons[1])
        # print(knop2)
        # if (not knop2 and (knop2_ingedrukt != knop2)):
        #     actie(16)
        #     knop2_ingedrukt = 0
        # knop3 = GPIO.input(buttons[2])
        # print(knop3)
        # if (not knop3 and (knop3_ingedrukt != knop3)):
        #     actie(12)
        #     knop3_ingedrukt = 0
        # knop4 = GPIO.input(buttons[3])
        # print(knop4)
        # if (not knop4 and (knop4_ingedrukt != knop4)):
        #     actie(25)
        #     knop4_ingedrukt = 0
        # time.sleep(0.5)
        # buzzer.lawaai_buzzer_add_frame()


except KeyboardInterrupt:
    GPIO.output(led,GPIO.LOW)
    GPIO.output(buzzer, GPIO.LOW)

GPIO.cleanup()
