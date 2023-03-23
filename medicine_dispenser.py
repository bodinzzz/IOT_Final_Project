import RPi.GPIO as GPIO
import time
 
CONTROL_PIN = 17
PWM_FREQ = 50  
STEP=15

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(CONTROL_PIN, GPIO.OUT)
 
pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)
pwm.start(0)
 
def angle_to_duty_cycle(angle=0):
    duty_cycle = (0.05 * PWM_FREQ) + (0.19 * PWM_FREQ * angle / 180)
    return duty_cycle
 
def test(num):
    number=int(num)
    try:
        #num=int(input("medicine_num:"))
        for i in range(number):
            dc = angle_to_duty_cycle(90)
            pwm.ChangeDutyCycle(dc)
            print('角度={: >3}, 工作週期={:.2f}'.format(90, dc))
            time.sleep(1)
            dc = angle_to_duty_cycle(0)
            pwm.ChangeDutyCycle(dc)
            print('角度={: >3}, 工作週期={:.2f}'.format(0, dc))
            time.sleep(1)
        
        pwm.ChangeDutyCycle(angle_to_duty_cycle(90))
        while True:
            next
    except KeyboardInterrupt:
        print('關閉程式')
    finally:
        pwm.stop()
        GPIO.cleanup()