# Untitled - By: HP - Sat Sep 10 2022


# Example of servo control.
#
# This example demonstrates the servo expansion board. Please follow the steps below:
#
# 1. Connect the servo to any PWM output.
# 2. Connect a 3.7v battery (or 5V power supply) to VIN and GND.
# 3. Copy pca9685.py and servo.py to OpenMV and reset.
# 4. Connect and run this script in the IDE.

import time # import clock
from servo import Servos    # Import the servo class
from machine import I2C, Pin    # Import I2C protocol and Pin definition

# Create an I2C object (I2C is a class)
i2c = I2C(sda=Pin('P5'), scl=Pin('P4')) # Set the sda ​​address of I2C to the P5 pin and the
# scl address to the P4 pin. This does not need to be changed

# Create two servo objects
servo = Servos(i2c, address=0x40, freq=50, min_us=500, max_us=2500, degrees=180)

    # Parameter 1: "i2c" means that we use the I2C protocol. Parameter 2:
    # "address=0x40" means that the address of I2C is 0x40 (0x40 is determined by
    # the parameters of the expansion board. If you want to solder the solder joint
    # on the back, change it to 0x60. see official website).
    # Parameter 3: "freq" indicates the frequency of the servo, which is related to
    # the servo we use. Parameter 4 and 5: "min_us and max_us" indicate the minimum
    # pulse width and the maximum pulse width, respectively, and need to be changed to
    # the same parameters as the servo ( See the official website for details).
    # Parameter 6: "degress" represents the angle

    # No. 2 servo needs to be changed to address 0x60 Since the same servo is used,
    # other parameters do not need to be changed
#servo2 = Servos(i2c, address=0x60, freq=50, min_us=500, max_us=2500, degrees=180)

# Cycle sixteen servos
while True:# i refers to the number of the servo, and it can be specified whether it is
           # the servo motion of servo1 or the servo motion of servo2.
    for i in range(0, 8):
        servo.position(i, 0)    # Control each servo to turn to 0° first
    time.sleep_ms(500)  # Delay 500ms

    for i in range(0, 8):
        servo.position(i, 180)  # Control each servo to turn to 180°
    time.sleep_ms(500)  # Delay 500ms


#    for i in range(0, 8):
#        servo2.position(i, 0)    # Control each servo to turn to 0° first
#    time.sleep_ms(500)  # Delay 500ms

#    for i in range(0, 8):
#        servo2.position(i, 180)  # # Control each servo to turn to 180°
#    time.sleep_ms(500)  # Delay 500ms


