"""
Illustrative LEGO Mindstorms EV3 line-following example using ev3dev2.

IMPORTANT:
- This is NOT the original competition source code.
- It has not been tested on the team's physical robot.
- Confirm motor/sensor ports and calibrate the threshold before use.
- This simple example uses reflected-light intensity as a steering signal;
  it does not identify green specifically without suitable calibration/logic.
"""

from time import sleep

from ev3dev2.motor import MoveTank, OUTPUT_B, OUTPUT_C, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1

# Adjust these ports to match your actual EV3 build.
LEFT_MOTOR_PORT = OUTPUT_B
RIGHT_MOTOR_PORT = OUTPUT_C
COLOR_SENSOR_PORT = INPUT_1

BASE_SPEED = 10       # Start slowly and tune after safe tests.
TARGET_REFLECT = 35   # PLACEHOLDER: measure the actual course first.
STEERING_GAIN = 0.20  # PLACEHOLDER: tune for the actual robot.
MAX_CORRECTION = 25
LOOP_DELAY_SECONDS = 0.02


def clamp(value, low, high):
    """Keep value within a numeric range."""
    return max(low, min(high, value))


def main():
    sensor = ColorSensor(COLOR_SENSOR_PORT)
    drive = MoveTank(LEFT_MOTOR_PORT, RIGHT_MOTOR_PORT)

    print("EV3 line-following starter example")
    print("Not the original competition program; calibrate before use.")
    print("Stop with Ctrl+C.")

    try:
        while True:
            reflected = sensor.reflected_light_intensity
            error = TARGET_REFLECT - reflected
            correction = clamp(
                error * STEERING_GAIN,
                -MAX_CORRECTION,
                MAX_CORRECTION,
            )

            left = clamp(BASE_SPEED + correction, -30, 30)
            right = clamp(BASE_SPEED - correction, -30, 30)
            drive.on(SpeedPercent(left), SpeedPercent(right))
            sleep(LOOP_DELAY_SECONDS)

    except KeyboardInterrupt:
        pass
    finally:
        drive.off()
        print("Motors stopped.")


if __name__ == "__main__":
    main()
