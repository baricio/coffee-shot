from LuckRoulette import LuckRoulette
import RPi.GPIO as GPIO
import time

def blink(time_count, channel):
    GPIO.output(channel,GPIO.HIGH)
    time.sleep(time_count)
    GPIO.output(channel,GPIO.LOW)
    time.sleep(time_count)
    half_time = time_count/1.5;
    if half_time > 0.001:
        blink(half_time, channel)

button = 21
led_button = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_button, GPIO.OUT, initial=GPIO.LOW)

while True:
    if GPIO.input(button) == GPIO.HIGH:
        print("começou o sorteio")
        blink(2, led_button)
        luckRoulette = LuckRoulette()
        luckRoulette.raffle()
    else:
        waiting = 1
        
    time.sleep(0.3)
