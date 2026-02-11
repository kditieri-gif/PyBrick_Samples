from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, Remote, UltrasonicSensor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

# Define objects for a simple two motor rover using a DriveBase 
hub = InventorHub()

left_motor = Motor(Port.C)
right_motor = Motor(Port.D)
eyes = UltrasonicSensor(Port.B)
down_eye = ColorSensor(Port.A)

# Color.WHITE = Color(h)

while True:
    if (down_eye.color() != Color.WHITE)
        left_motor.run(-100)
        right_motor.run(100)
        wait(50)
    else:
        left_motor.stop()
        right_motor.stop()
        wait(50)
        left_motor.run(100)
        right_motor.run(-100)
        wait(2000)
        left_motor.run(100)
        right_motor.run(100)
        wait(100)



    # if down_eye == WHITE:
    #         left_motor.stop()
    #         right_motor.stop()
    #         wait(5000)
    #         # Robot moves straight
    #         left_motor.run(-100)
    #         right_motor.run(100)
    #         wait(50)
    # else:
    #     if eyes.distance() < 500:
    #         # If something is in front, stop robot motion
    #         left_motor.stop()
    #         right_motor.stop()
    #         wait(5000)
    #     else:
    #         # Robot moves straight
    #         left_motor.run(-100)
    #         right_motor.run(100)
    #         wait(50)


