# Odometry Calibration {#odometry_calibration status=draft}

Assigned: Jacopo

<!-- From old google docs file: https://docs.google.com/document/d/1FmuOvPtKPMSIfay0wuxPQXESbmxYewl3gwJmhLU-4KY/edit#

Motivation
You might have noticed that your vehicle doesn’t really go in a straight line when you command it to. Also, the vehicle might not go at the velocity you are commanding it to drive at.

This is due to the fact a slight difference between the motors and the wheels can cause the left wheel and right wheel to travel slightly different distance even though they have made the same rotation. Also, the system has no encoders, so we are commanding open loop voltages without ensuring the desired wheel velocity is met.

We can counter this behavior by calibrating the “gain” and “trim”  on the commands that are sent to the wheels. This tutorial will walk you through the calibration process and also introduce the use of parameter server in ROS.
Method
We want to be able to specify a velocity(speed) and angular velocity(rotation) to control where the car goes. However the motors can only be controlled via rotation rate commands. Our robots use differential drive. For details see https://chess.eecs.berkeley.edu/eecs149/documentation/differentialDrive.pdf

Software Implementation
The inverse_kinematics_node under dagu_car pkg is in charge of translating a desired velocity(speed) and angular velocity(rotation) command, also called Twist2D, to motor voltages. It also adjusting the wheel voltage commands by a gain and trim value. The relationship between the velocities and the output voltages are defined as:

right_wheel_voltage = (gain + trim) * (linearVelocity + angularVelocity * 0.5 * baseline)
left_wheel_voltage = (gain - trim) * (linearVelocity - angularVelocity * 0.5 * baseline)

The baseline is the distance between the two wheels. Note that if the gain = 1.0 and trim = 0.0, the wheel’s voltages are exactly the same as the linear velocity + or - angular velocity times half the baseline length.


With gain > 1.0, the vehicle goes faster given the same velocity command, and for gain <1.0 it would go slower.

With trim > 0, the right wheel will turn slightly more than the left wheel given the same velocity command; with trim < 0, the left wheel will turn slightly more the right wheel.
Calibration Instructions
Make sure that your vehicle is on and connected to the wifi.

On your Duckiebot, launch the joystick

duckiebot: $ roslaunch duckietown_demos joystick.launch veh:=${VEHICLE_NAME}

Changing the trim to 0.01:

duckiebot: $ rosservice call /${VEHICLE_NAME}/inverse_kinematics_node/set_trim -- 0.01

Or Changing the trim in a negative way, e.g. to -0.01:

duckiebot: $ rosservice call /${VEHICLE_NAME}/inverse_kinematics_node/set_trim -- -0.01

Keep setting the trim until the duckiebot goes straight

Then start setting the gain:

duckiebot: $ rosservice call /${VEHICLE_NAME}/inverse_kinematics_node/set_gain -- 1.1

When you are all done, save the parameters by running:

duckiebot: $ rosservice call /${VEHICLE_NAME}/inverse_kinematics_node/save_calibration

If you do this the first time, you will see how it creates a new ${VEHICLE_NAME}.yaml file for your duckiebot in the folder:
duckietown/config/baseline/calibration/kinematics
 which you can add and commit to the git repo.

Testing instructions
See operation manual instructions for details
Demo instructions
You can connect to your robot and just run “make demo-joystick” to play around with driving straight and  changing the trim/gain
Performance Evaluation
The trim performance is tested by setting a reasonable distance (3 tiles length) and evaluating whether or not the robot can stay within the lane when it traverse the entire distance. The velocity is tested similarly by evaluating whether the robot traverses far enough or too far when driving for a specific amount of time.


-->
