# Hardware and control notes

## Confirmed project details

- Platform: LEGO Mindstorms EV3.
- Programming language: Python.
- Competition objective: follow a green path and collect flags.
- Result: 3rd place; 80% of flags collected.

## Details still to verify from the physical robot

| Component or behavior | Current status | What to document |
|---|---|---|
| EV3 software/OS | Not confirmed | ev3dev version or other Python environment |
| Drive motors | Not confirmed | Motor type and output ports |
| Path sensor | Not confirmed | Sensor model, port and mounting height |
| Green detection | Not confirmed | Color mode or calibrated reflectance threshold |
| Steering logic | Not confirmed | Threshold, proportional/PID or other control method |
| Flag mechanism | Not confirmed | Attachment, actuator and collection sequence |
| Operating speed | Not confirmed | Speed values and tuning rationale |

## Calibration checklist

1. Record sensor values over the green path and the surrounding surface under the lighting used for the course.
2. Check whether the chosen sensor mode can distinguish green from the background.
3. Select thresholds based on real readings rather than the placeholder value in the example.
4. Verify motor direction and steering correction with the wheels lifted or at low speed in a clear area.
5. Increase speed only after stable behavior is confirmed.
6. Test the flag-collection mechanism separately before combining it with autonomous driving.

## Example-code limitation

The current sample uses reflected-light intensity as a simple feedback signal. Reflected-light intensity is not automatically a green-color detector; the correct sensor mode and logic depend on the actual hardware and course surfaces. The target value, steering gain and port assignments are placeholders.

## Safety

- Keep the robot on a clear, low surface during initial tests.
- Stay close to the stop control and do not run unattended.
- Stop immediately if steering is unstable or the robot leaves the course.
