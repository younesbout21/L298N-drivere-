from machine import Pin, PWM
import time

# Defining motor pins

# OUT1 and OUT2
In1 = Pin(6, Pin.OUT) 
In2 = Pin(7, Pin.OUT)  
EN_A = Pin(17, Pin.OUT)

# OUT3 and OUT4
In3 = Pin(4, Pin.OUT)  
In4 = Pin(3, Pin.OUT)  
EN_B = Pin(2, Pin.OUT)

EN_A.high()
EN_B.high()

# Define motor speed variable
motor_speed = 0.1  # set to minimum speed initially

# Create PWM objects for motor control pins
pwm1 = PWM(In1)
pwm2 = PWM(In2)
pwm3 = PWM(In3)
pwm4 = PWM(In4)

# Set PWM frequency to 1kHz
pwm1.freq(1000)
pwm2.freq(1000)
pwm3.freq(1000)
pwm4.freq(1000)

# Define maximum and minimum speeds
max_speed = 0.5
min_speed = 0.1

# Stop
def stop():
    pwm1.duty_u16(0)
    pwm2.duty_u16(0)
    pwm3.duty_u16(0)
    pwm4.duty_u16(0)

# Increase and decrease speed continuously
while True:
    # Increase speed step by step
    for speed in range(int(min_speed * 100), int(max_speed * 100), 5):
        motor_speed = speed / 100
        pwm1.duty_u16(int(65535 * motor_speed))
        pwm2.duty_u16(0)
        pwm3.duty_u16(int(65535 * motor_speed))
        pwm4.duty_u16(0)
        time.sleep(1)
    
    # Decrease speed step by step
    for speed in range(int(max_speed * 100), int(min_speed * 100), -5):
        motor_speed = speed / 100
        pwm1.duty_u16(int(65535 * motor_speed))
        pwm2.duty_u16(0)
        pwm3.duty_u16(int(65535 * motor_speed))
        pwm4.duty_u16(0)
        time.sleep(1)
    
    # Stop the motors at minimum speed
    stop()
    motor_speed = min_speed
