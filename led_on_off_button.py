import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
Button=19
GPIO.setup (Button,GPIO.IN,pull_up_down=GPIO.PUD_UP)

Led=21
GPIO.setup(Led,GPIO.OUT)

while True:
    input_state= GPIO.input(Button)
    if input_state == 0:
        print(input_state)
        GPIO.output(Led,1)
        time.sleep(2)
    else:
        GPIO.output(Led,0)
        time.sleep(2)
        print(input_state)
GPIO.cleanup()
