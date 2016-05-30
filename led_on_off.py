import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
led=26
for i in range(0,10):
  GPIO.setup(led,GPIO.OUT)
  GPIO.output(led,1)
  time.sleep(1)
  GPIO.output(led,0)
  time.sleep(1)
GPIO.output(led,0)
GPIO.cleanup()
