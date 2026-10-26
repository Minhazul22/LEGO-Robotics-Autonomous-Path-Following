# LEGO Robotics Competition: Autonomous Path-Following Robot

<p align="center">
  <strong>LEGO Mindstorms EV3 · Python · Autonomous navigation</strong><br>
  University robotics competition — project “Chicken Lady”
</p>

<p align="center">
  <img alt="Platform" src="https://img.shields.io/badge/Platform-LEGO%20Mindstorms%20EV3-CC0000">
  <img alt="Language" src="https://img.shields.io/badge/Language-Python-3776AB">
  <img alt="Result" src="https://img.shields.io/badge/Competition-3rd%20place-success">
</p>

A university robotics competition project focused on a LEGO Mindstorms EV3 robot that followed a green path and collected flags. The team placed **3rd**, collecting **80% of the flags**.

> **Code provenance:** The original competition source code was not available. `src/line_following_example.py` is an illustrative starting point using the `ev3dev2` API. It is not the original program and has not been tested on the team's physical robot.

## Project at a glance

| Item | Details |
|---|---|
| Robot platform | LEGO Mindstorms EV3 |
| Programming language | Python |
| Navigation task | Follow a green path |
| Secondary objective | Collect flags |
| Competition result | **3rd place** |
| Reported performance | **80% of flags collected** |
| Project name in presentation | Chicken Lady |

## Highlights

- Planned the team's game strategy and overall approach.
- Coordinated team tasks and deadlines.
- Designed the flags used in the project.
- Contributed to an autonomous path-following and flag-collection challenge.
- Achieved 3rd place, with 80% of the flags collected.

## How the task can be understood

At a high level, the competition task involved detecting and following a green path, navigating the course, and collecting flags. The exact sensor model, motor ports, flag mechanism, and control algorithm used in the competition have not yet been verified from the available source materials.

## Illustrative Python example

A starter example is provided in [`src/line_following_example.py`](src/line_following_example.py). It demonstrates a basic feedback loop with reflected-light readings and differential motor speeds.

**Important:** this sample uses a placeholder reflected-light target; it does not, by itself, detect the color green specifically. It is for learning and adaptation, not a verified reconstruction of the competition robot. Confirm the EV3 operating system, sensors, ports, and calibration before use.

See [Hardware and control notes](docs/hardware-and-control.md) before attempting to run the example.

## Repository structure

```text
.
├── README.md
├── src/
│   ├── README.md
│   └── line_following_example.py
├── docs/
│   ├── project-notes.md
│   ├── hardware-and-control.md
│   └── Team07-Chicken-Lady-presentation.pdf
└── media/
    └── README.md
```

## Results

- **Competition placement:** 3rd
- **Flags collected:** 80%
- **Main challenge:** autonomous green-path following and flag collection

## My contribution

- Led project management and defined the game plan.
- Designed the flags.
- Coordinated team tasks and deadlines.

## Media and evidence

Add approved project photos and a short demonstration video to the `media/` directory, then link them here. The repository currently includes documentation and an illustrative controller; original competition code and media still need to be added if available. Only publish files you have permission to share, and remove personal information from public media.

## Future improvements

- Recover or recreate the original EV3 Python program and label any recreation accurately.
- Confirm the color sensor model, motor ports, and flag mechanism.
- Document the actual green-path detection and steering approach.
- Add a course diagram and a short robot demonstration video.
- Record repeatable test results and explain what was changed during testing.

---
*This repository separates confirmed project results from illustrative code and unverified hardware details.*
