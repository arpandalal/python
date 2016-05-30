import time
import RPi.GPIO as GPIO
times = int(input("Enter blink times:"))
GPIO.setmode(GPIO.BCM)
led=21
for i in range(0,times):
  GPIO.setup(led,GPIO.OUT)
  GPIO.output(led,1)
  time.sleep(0.5)
  GPIO.output(led,0)
  time.sleep(0.5)
GPIO.output(led,0)
GPIO.cleanup()
