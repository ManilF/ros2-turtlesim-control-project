# ROS 2 Turtlesim Control Project

This project is a ROS 2 workspace experiment built around `turtlesim`. It implements a custom ROS 2 Python node that repeats velocity commands with timeout-based safety behavior and exposes a custom service for computing the direction and distance from the turtle's current pose to a requested target position.

The goal of the project was to practice ROS 2 communication patterns used in robotics software: publishers, subscribers, timers, custom interfaces, service servers, and pose-based control logic.

## What It Does

- Repeats velocity commands from `/turtle1/cmd_vel` onto `/turtle1/cmd_vel_repeat`.
- Publishes a zero-velocity command when no recent command has been received, preventing stale commands from continuing indefinitely.
- Subscribes to `/turtle1/pose` to track the turtle's current position and heading.
- Provides a `/set_pose` service that returns the distance and heading correction needed to face a target `(x, y)` position.

## Packages

```text
ros2-turtlesim-control-project/
├── turtlesim_ferr/
│   └── Python ROS 2 package containing the turtlesim control node
├── turtlesim_ferr_interfaces/
│   └── Custom ROS 2 interface package defining SetPose.srv
├── Part2.md
└── Part3.md
```

## Technical Details

The main node is `turtle_repeater` in `turtlesim_ferr`.

It uses:

- `geometry_msgs/Twist` for velocity command input and output
- `turtlesim/Pose` for live turtle state feedback
- a timer callback to enforce command freshness
- a custom `SetPose` service for target-distance and angle calculations

The custom service is defined as:

```text
float64 x
float64 y
---
float64 distance
float64 angle
```

Given a target position, the service computes:

- Euclidean distance from the current turtle position to the target
- normalized heading error in the range `(-pi, pi]`

## Build

From the workspace root:

```bash
colcon build
source install/setup.bash
```

On Windows PowerShell with a ROS 2 environment already sourced:

```powershell
colcon build
.\install\setup.ps1
```

## Run

Start `turtlesim`:

```bash
ros2 run turtlesim turtlesim_node
```

In another terminal, run the custom node:

```bash
ros2 run turtlesim_ferr turtle_repeater
```

Send a service request:

```bash
ros2 service call /set_pose turtlesim_ferr_interfaces/srv/SetPose "{x: 5.0, y: 5.0}"
```

## Project Status

This is an early ROS 2 learning project focused on core robotics software concepts. Future improvements could include adding a closed-loop controller that automatically drives the turtle toward the requested target pose, improving launch files, and adding tests for the service math.
