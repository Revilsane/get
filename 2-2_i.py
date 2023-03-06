import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
def foo(number):
    dac = [10, 9, 11, 5, 6, 13, 19, 26]
    GPIO.setup(dac, GPIO.OUT)
    l=len(dac)
    for i in range(l):
        GPIO.output(dac[i], number[i])
    time.sleep(15)
    GPIO.output(dac, 0)
r = bin(255)
number = [int(j) for j in r[2::]]
GPIO.cleanup()
