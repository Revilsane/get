import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
r=bin(255)
dac = [10, 9, 11, 5, 6, 13, 19, 26]
number = [int(j) for j in r[2::]]
p = number[::-1]
if len(number)!=8:
    for k in range(8-len(number)):
        p.append(0)
    GPIO.setup(dac, GPIO.OUT)
    l=len(dac)
    for i in range(8):
        GPIO.output(dac[i], p[i])
    time.sleep(15)
    GPIO.output(dac, 0)
    GPIO.clenup()
if len(number)==8:
    GPIO.setup(dac, GPIO.OUT)
    l=len(dac)
    for i in range(8):
        GPIO.output(dac[i], p[i])
    time.sleep(15)
    GPIO.output(dac, 0)
    GPIO.clenup()
print(p)
