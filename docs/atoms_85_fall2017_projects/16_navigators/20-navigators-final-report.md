# Navigators: final report {#navigators-final-report status=ready}


TODO: JT: add operation manual, fix bibliographic references, math formatting, various typos

## The final result {sec:navigators-final-result}

Video of the final result:

<div figure-id="fig:demo_video_navigators">
    <figcaption>The Navigators Demo Video</figcaption>
    <dtvideo src="vimeo:257911020"/>
</div>



## Mission and Scope {#navigators-final-scope}

The objective of this project was to implement a method that allows Duckiebots to reliably navigate any kind of intersection they may encounter when driving through a regular Duckietown.

Motto:

TRANSIBITIS (you shall pass)

What is in scope:

* Navigating three- and four-way intersections of predetermined shape.
* Absolute localization within the intersection.
* Computing a path that guides the Duckiebots across the intersection to the desired exit.
* Tracking the path.
* Detecting when the Duckiebot successfully navigates across the intersection and finds itself in a regular lane.
* Limiting travel time across intersection.

### Motivation {#navigators-final-result-motivation}

We seek to find a method that allows a Duckiebot to safely navigate an intersection. Duckiebots navigate through regular streets in Duckietown using a lane following method. It includes a localization method but also a position control method. Based on this scheme, the need for a controlled crossing of intersection emerged. The main motivation is therefore based on the safety and the reliability of intersection navigation. Ideally, the vehicle should be able to not only go from exit 1 to exit 2, but also recognize where it is relative to those 2 points (localization). Once the Duckiebot receives information about its current position, it will be able to correct any mistake relative to a precalculated path.

### Existing solution {#navigators-final-literature}

The project starts from the current solution, in which the Duckiebot navigates the intersections in open loop. In this solution, after arriving at an intersection, the Duckiebot uses the AprilTags to know the kind of intersection and the feasible exits. Then it randomly chooses one of them and executes standard commands to navigate. This solution did not include localization implying that the current position of the vehicle was not known during the intersection navigation. Since one of the objectives of the project was to use the controller, that the Controllers group designed, the open loop implementation could not be used any further. For practical reasons, we almost started from scratch, and the new solution would have very few common points with the previous implementation.

So our main improvement to the current solution is the use of the camera to introduce vision during navigation. This allow us to introduce feedback into the system with all the benefits that closed loop control has with respect to open loop, and so regulating the control inputs based on the information of the system state.

### Opportunity {#navigators-final-opportunity}

As mentioned previously, the drawback of the existing solution is the missing information about the Duckiebot’s position during the navigation. The result is that the system inputs, linear and angular velocities are independent of the system state so that the navigation is not robust and the percentage of failures is high (around 50% for some group members’ Duckiebots for short right turns).

Our main contribution is to use the camera as well as a state estimator to estimate the absolute position of the robot with respect to the intersection. Moreover, we compute a path to the desired exit. The planned path is a cubic spline computed with two control points and directions, placed in the initial and final desired intersection positions.

The localization is done by comparing the images from the camera with a template of the intersection. Namely, edges are detected in the current image and some control points are defined so to minimize the distance between their 2D projections in the image frame and the detected edges. In this way, we can estimate the initial position and localize our robot during the navigation.

Reference paper, from which we took inspiration is J. Barandiaran, D.Borro, “Edge-Based Markerless 3D Tracking of Rigid Objects”, IEEE Conference on Artificial Reality and Telexistence, 2007.

## Definition of the problem {#navigators-final-problem-def}

### Problem Statement

We seek to find a method that allows a Duckiebot to safely navigate an intersection. In particular, we attempt to solve the following problem: Given that the Duckiebot finds itself at rest at an intersection, 1) Initial localization of the rest position, 2) compute a path that guides the Duckiebot to the desired exit while respecting the Duckiebots’ system dynamics and control input limitations, 3) Continuous localization thanks to a state estimator which integrates wheel commands and pose updates from images, the same method of the initial localization is used frame by frame, 4) track the path providing localization feedback to the lane controller, and lastly 5) detect when the maneuver is finished and the Duckiebot finds itself in a regular lane.

### Assumptions

* Size, shape of intersections are given and fixed.
* Color and size of lane markings are given and fixed.
* The type of intersection (e.g. three-way or four-way intersection) as well as the desired exit (e.g. left turn, right turn or straight) are provided.
* There are fiducial markers, mainly AprilTags, placed at the intersection at predetermined positions.
* The Duckiebots are initially at rest and their pose is within a certain range with respect to the intersection (distance to center of road, distance to stop line, orientation within the lane).
* The intersection is free of obstacles.
* Good light conditions (e.g. no illumination problems, ...)

### Stakeholders

* Smart Cities
* The Controllers
* Fleet planning
* Coordinators

<div figure-id="fig:stakeholders" figure-caption="Stakeholders Diagramm">
    <img src="stakeholders_diagram.png" style="width: 60%"/>
</div>

### Performance measurement

Success rate, i.e. the percentage of trials for which the Duckiebot ends up in the desired lane and successfully hands over the control to the lane following controller. A trial is considered to be successful if the Duckiebot is completely inside the desired lane without touching any lane markings. The success rate is evaluated by simply performing the intersection navigation task N times and counting the number of successful trials.
Accuracy and precision of final state, i.e. how close is the Duckiebot’s state relative to the desired final state and how repeatable is this. The accuracy and precision of the final state is estimated using the existing lane detection method, and is measured for different initial conditions.
Duration, i.e. the average time required for the Duckiebot to cross an intersection and an upper limit (worst-case) on the time required. The average duration is computed by running a series of N experiments.

## 4 Contribution / Added functionality {#navigators-final-contribution}

<div figure-id="fig:2" figure-caption="Logical architecture diagramm">
    <img src="logical_architecture_diagram.png" style="width: 100%"/>
</div>

The intersection navigation is started as soon as the Duckiebot is told that it is in front of an intersection. The following functions are then executed (in chronological order):
* The Duckiebot localizes itself with respect to the intersection, given the intersection type.
* The Duckiebot waits until it receives a message “turn_type” indicating which exit of the intersection it should take, and a message “go” indicating that the navigation can start.
* A path is planned that guides the Duckiebot from its current location to the desired intersection exit.
* The lane following controller, adapted for path tracking, steers the Duckiebot to its final location. During the navigation, the Duckiebot continuously localizes itself and feeds the estimated pose (i.e. the distance from the desired path and the relative orientation error) to the lane following controller to account for disturbances or modelling errors.
* The Duckiebot detects when it traversed the intersection, i.e. when it finds itself again in a regular lane, and hands control back to the lane following controller by publishing on the topic “intersection_done”.

It is assumed that:
* the Duckiebot stops between 0.10m and 0.16m in front of the center of the red stop line, i.e. $d_x \in \lbrack 0.1m,0.16m\rbrack$, has an error of no more than 0.03m with respect to the center of its lane, i.e. $d_y \in \lbrack-0.03m,0.03m\rbrack$, and that the orientation error is smaller than 0.17rad, i.e. $\theta\in\lbrack-0.17rad,0.17rad\rbrack$ (see Fig. 4 for details, all values are with respect to the origin of the Duckiebot’s axle-fixed coordinate frame).
* a lane following controller exists that takes as inputs the distance from desired path $d$ and the orientation error with respect to the path tangent $\theta$ (see Fig. 5 for details).
This is done by the new lane following controller. However, we needed to slightly modify
the controller to account for thresholds wheels’ speed.

<div figure-id="fig:3" figure-caption="Duckiebot's position relative to the red line.">
    <img src="duckiebot_red_line.png" style="width: 100%"/>
</div>

<div figure-id="fig:4" figure-caption="Duckiebot's pose relative to the desired path.">
    <img src="duckiebot_path.png" style="width: 100%"/>
</div>

### Software architecture

Two nodes were developped: *“intersection_navigation”* and *“intersection_localization”*. In the following, their functionality and interfaces will be described in detail.

**“intersection_navigation”-node**

The *“intersection_navigation”*-node is responsible for the high level logic of navigating the Duckiebot across an intersection, planning paths from the Duckiebot’s initial position to the final position, estimating the Duckiebot’s pose and communicating with the lane following controller. It subscribes to the following topics:

* “~fsm”: Used to detect when Duckiebot is at an intersection or when the intersection control is active, respectively. As soon as the mode is switched to “INTERSECTION_COORDINATION”, the *“intersection_navigation”*-node will take over.
* “~turn_type”: Tells the Duckiebot the type of turn it should take (e.g. left, right, straight, random).
* “~pose_in”: Measured pose of the “intersection_localization”-node with respect to an inertial frame $\mathcal{I}$ (see Fig. 5). This message is used to estimate the pose of the Duckiebot at the intersection, which is then used by the controller to follow the desired pose. This message will have quite some delay (several 10ms), but the delay will be compensated by a state estimator using the timestamp of the message (i.e. camera frame) and using the past commands sent to the vehicle.
* “~image/compressed": Upon receiving such a message, the Duckiebot's pose at the time the image was taken will be estimated and sent to the *"intersection_localization"*-node to initialize the localization problem.
* “~cmds”: The command published by the “forward_kinematics_node”, linear and angular velocities. These commands are stored in a queue and will be used to compensate for delays and to predict the Duckiebot’s pose.
* “~in_lane”: The command published by the lane filter. It is true when the robot finds itself in lane.

The “intersection_navigation”-node publishes on the following topics:

* “~intersection_done”: A message on this topic will be broadcasted as soon as the Duckiebot finished traversing the intersection and is used to handback the control.
* "~pose_img_out": Estimated pose of the Duckiebot with respect to an inertial frame $\mathcal{I}$ at the time when the camera image is taken. This topic is subscribed by the “intersection_localization”-node in order to initialize the localization problem.
* “~intersection_navigation_pose”: Pose of the Duckiebot with respect to the desired path (see Fig. 5). This topic is basically identical to the “~lane_pose”-topic from the lane filter and will be used by the “lane_controller”-node in case “fsm” is “INTERSECTION_CONTROL”.

**“intersection_localizer”-node**

The *“intersection_localization”*-node is responsible for localizing the Duckiebot at an intersection. For this purpose, it subscribes to the following topics:

* “~pos_img_in”: The predicted pose of the Duckiebot with respect to an inertial frame at the time when the camera image was taken as well as the raw image from the camera. This information will be used to initialize the localization problem this node solves. Since the Duckiebot’s pose is predicted for the time the camera image was taken, delays are irrelevant.

The *"intersection_localizer"*-node publishes the following topic:

* "~pose_out": This is the measured pose of the Duckiebot at the intersection with respect to an inertial frame $\mathcal{I}$ based on the received camera image. The measured pose will be timestamped with the timestamp of the camera image such that the "intersection_navigation"-node can compensate for the latency.
* "~localizer_debug_out": This topic is used in the visualizer node. The visualizer node can  be launched on the laptop, it allows to visualize the current frames and the estimated position.

<div figure-id="fig:6" figure-caption="Pose of the duckiebot with respect to the Inetial Frame.">
    <img src="bot_in_intersection.png" style="width: 100%"/>
</div>

### Algorithms

There are two main algorithms in our implementation about localization and path planning respectively

#### Localization algorithm:

The algorithm is composed by the following steps:

* Process raw image: The image from the camera is processed. The processing is composed by the rectification, conversion to gray scale and edges detector by the Canny edges algorithm.
* Compute pose: The current pose is estimated. The algorithm starts from a range of poses centered in the previous pose, for the initial localization we use information from the nearest April tag detected at intersection. We use a range of +- 2.5 cm and +- 5 deg around the pose to make the following optimization more robust with respect to not accurate enough camera calibration.
Next step is to compute control points from the template model along with their 2D projections onto the image plane.
In order to do it, we defined different templates which contain edges of the intersections.
The next step is a least squares optimization, defined as (Formula from the paper cited in [](#navigators-final-opportunity)):

\begin{equation}
W=min\sum_i (A_iW-l_i)^2
\end{equation}

Where A is the nx3 matrix which contains the n control points, W is the motion vector defined as $W=\lbrack w_z t_x t_y \rbrack^T$ where we can obtain the Rotation matrix from the vector w applying the Rodriguez’s formula. And l_i are the displacements between the projections of the control points and the edges detected in the image.

Then we obtain the new pose from W, which tells us the relative position and orientation between two consecutive poses, and the previous pose.

#### Path planning algorithm:

The path planned to traverse an intersection is a polynomial of order three. The polynomial coefficients are chosen such that the path starts at the Duckiebot’s current pose (i.e. position and orientation) and ends at a desired pose. However, this only defines the coefficients partially. In particular, the orientation of the Duckiebot only determines the direction of the velocity at the initial and final position, but not its magnitude. The magnitude of the initial and final velocity are thus optimized to minimize the curvature of the path. During the optimization, it is also verified that path does not contain any loops and that it satisfies the Duckiebot’s maximum curvature, i.e. only feasible paths are planned.

## Formal performance evaluation / Results {#navigation-final-formal}

### Performance evaluation

All the experiments are taken in a duckietown with appearence in accord to [appearance specifications](#duckietown-specs).
It is a Duckietown with 3 and 4-ways intersections and intersection April Tags well visible.
We consider an experiment is valid, when the Duckiebot correctly stops at the red line. The term correctly refers to the thresholds defined in section 8 Logical Architecture.
We let the Duckiebot navigate Duckietown for 2 runs of 30 minutes randomly choosing the exit to take.

* Success rate: Our implementation has success rate of 80% for the upper left turns and for the straight exit, whereas a lower rate of 65 % for the short right turn. The main failures are: right wheel touches the track boundary white line for the upper left turn, left wheel touches the middle dashed line for the straight exit and the right turn.
Mainly the lower success rate of the right turn is due to the fact that in such short maneuver the feedback controller cannot compensate, factors as wheels slippage and inaccurate kinematic calibration.
However, our implementation improves the current solution, in which the Duckiebots hits a lane marking 50% of the times and often fails in navigating the short right turn.

* Accuracy and precision: We define a final state as accurate when the Duckiebot finds itself in lane after the intersection navigation is done. Our results show that 95% of the times that the navigation is concluded the robot detects itself in lane and successfully switches to the lane following control.
To note that, if the path is concluded but the robot does not find itself in lane, it slows down and goes straight for 2 seconds. If it finds itself in lane during this time, we hand back the control over to the lane following controller, otherwise the robot stops.

* Duration of the intersection: The time is computed from when the Duckiebot arrives at the red line, the fsm mode is at “intersection_coordination”, and the intersection navigation is done, publishing of the topic “intersection_done”.
The average time is 17 seconds and the upper limit (worst-case) is 21 seconds.

Moreover, we estimate the accuracy and precision of the estimated pose during traversing the intersection with a visualizer node, which can be run on the laptop. The visualizer node outputs the images from the camera and the edges projections from the estimated current pose.

The time between when the Duckiebot stops at the red line and when it is ready to start the navigation as well as the pose estimation accuracy are the biggest challenges, where mainly our solution may be improved.

In the next section, we give some insights about a possible ways of improvement.

## Future avenues of development {#navigators-final-next-steps}

The main improvements can be done about the accuracy of the localization, which will also have a positive impact on the computation time.

Specifically, our localization algorithm is very sensible to the camera calibration. Since the calibration matrices are used in the 2D projection of the control points in the image frame, with not adequately good calibration, the optimization problem will minimize quantities that are affected by offsets. In order to compensate for it we optimize, as described in section 8 Algorithms, over a range of initial conditions, but this increases the computation time.

A solution could be to improve the camera calibration procedure and introducing metrics to evaluate its performance. It would allow to decrease the range of initial positions used in the least squares optimization and so to have benefits on both localization accuracy and computation time.
