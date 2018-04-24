#  Navigators: intermediate report {#navigators-int-report status=ready}

TODO: JT: fix intra-duckiebook links

## Part 1: System interfaces


### Logical architecture


<div figure-id="fig:simple-step-diagram" figure-caption="Simple step diagram">
    <img src="logicaldiagram2.png" style="width: 60%"/>
</div>

The intersection navigation is started as soon as the Duckiebot is told that it is in front of an intersection. The following functions are then executed (in chronological order):

* The Duckiebot localizes itself with respect to the intersection.

* The Duckiebot waits until it receives a message on the topic “turn_type” which exit of the intersection it should take.

* A path is planned that guides the Duckiebot from its current location to the desired intersection exit.

* A path following controller steers the Duckiebot to its final location, while the Duckiebot continuously localizes itself and feeds the estimated pose (i.e. the distance from the desired path and the relative orientation error) to the lane following controller to account for, for example, disturbances or modelling errors.

* The Duckiebot detects when it traversed the intersection, i.e. when it finds itself again in a regular lane, and hands control back to the lane following controller by publishing on the topic “intersection_done”.


It is assumed that

* the Duckiebot stops between 0.10m and 0.16m in front of the center of the red stop line, i.e. $d_x \in \lbrack 0.1m,0.16m\rbrack$, has an error of no more than 0.03m with respect to the center of its lane, i.e. $d_y \in \lbrack-0.03m,0.03m\rbrack$, and that the orientation error is smaller than 0.17rad, i.e. $\theta\in\lbrack-0.17rad,0.17rad\rbrack$ (see Fig. 1.2 for details, all values are with respect to the origin of the Duckiebot’s axle-fixed coordinate frame).

* a lane following controller exists that takes as inputs the distance from desired path $d$ and and the orientation error with respect to the path tangent $\theta$ (see Fig. 1.3 for details).


<div figure-id="fig:2" figure-caption="Pose of the duckiebot in front of an intersection">
    <img src="duckiebot_red_line.png" style="width: 100%"/>
</div>



<div figure-id="fig:3" figure-caption="Pose of the duckiebot relative to the desired path">
    <img src="duckiebot_path.png" style="width: 100%"/>
</div>



### Software architecture

We will develop two nodes; *“intersection_navigation”* and *“intersection_localization”*. In the following, their functionality and interfaces will be described in more detail.


**“intersection_navigation”-node**


The *“intersection_navigation”*-node is responsible for the high level logic of navigating the Duckiebot across an intersection, planning paths from the Duckiebot’s initial position to the final position, estimating the Duckiebot’s pose and communicating with the lane following controller. It subscribes to the following topics:

* “mode”: Used to detect when Duckiebot is at an intersection or when the intersection control is active, respectively. No assumptions about the latency of this topic will be made. As soon as the mode is switched to “INTERSECTION_CONTROL”, the *“intersection_navigation”*-node will take over.

* “turn_type”: Tells the Duckiebot the type of turn it should take (e.g. left, right, straight, random). No assumption about the latency of this topic will be made. As soon as message is received, the maneuver will be executed.

* “intersection_pose_meas_inertial”: Measured pose of the *“intersection_localization”*-node with respect to an inertial frame $\mathcal{I}$ (see Fig. 1.4). This message is used to estimate the pose of the Duckiebot at the intersection, which is then used by the controller to follow the desired pose. It is assumed that this message will have quite some delay (several 10ms), but the delay will be compensated by a state estimator using the timestamp of the message (i.e. camera frame) and using the past commands sent to the vehicle.


* “~image/compressed": Upon receiving such a message, the Duckiebot's pose at the time the image was taken will be estimated and sent to the *"intersection_localization"*-node to initialize the localization problem.

* “~car_cmd”: The command published by the “lane_controller”-node used to track a desired path. These commands are stored in a queue inand will be used to compensate for delays and predict the Duckiebot’s pose. It is assumed this topic has no delay, i.e. that commands are immediately executed.


The “intersection_navigation”-node publishes on the following topics:

* “intersection_done”: A message on this topic will be broadcasted as soon as the Duckiebot finished traversing the intersection and is used to handback the control.

* "intersection_pose":  Pose of the Duckiebot with respect to the desired path (see Fig. 3). This topic is basically identical to the “~lane_pose”-topic from the lane filter and will be used by the *“lane_controller”*-node in case “mode” is “INTERSECTION_CONTROL”.

The “intersection_navigation”-node will be estimated to introduce no more than 500ns  of delay in regular operation (it only does some logic) and hence an equal delay will be introduced to all the published topics. Initially, after the “intersection_localization”-node is initialized (see below), a path that guides the Duckiebot across the intersection will be planned. This task can be computationally expensive since it needs to be guaranteed that the path is feasible (e.g. not leaving the intersection, curvature constraints, …) and may take up to 500ms. However, since the Duckiebot is at rest at the intersection, this will not cause any issues.



**“intersection_localization”-node**


The *“intersection_localization”*-node is responsible for localizing the Duckiebot at an intersection. For this purpose, it subscribes to the following topics:

* “mode”: This topic is used to detect when the node should start localizing itself at an intersection. No assumption about its latency is made, since it is irrelevant for the node. As soon as the mode is switched to “INTERSECTION_CONTROL”, the *“intersection_localization”*-node will start to estimate the Duckiebot’s pose relative to the intersection.

* “~image/compressed”: The compressed camera image is used to localize the Duckiebot within the intersection. No assumption about the latency of this topic is made. In order to compensate for the expected latency, the timestamp of the camera frame will be also be used to indicate the time for which the pose is estimated.

* "intersection_pose_pred_inertial": The predicted pose of the Duckiebot at the time when the camera image was taken. This information will be used to initialize the localization problem this node solves. Since the Duckiebot’s pose is predicted for the time the camera image was taken, delays are irrelevant.


The *"intersection_localization"*-node publishes the following topic:

* "intersection_pose_meas_inertial": This is the measured pose of the Duckiebot at the intersection with respect to an inertial frame $\mathcal{I}$ based on the received camera image. The measured pose will be timestamped with the timestamp of the camera image such that the *"intersection_navigation"*-node can compensate for the latency.


It is estimated that it will take approximately 15ms to estimate the Duckiebot's pose once the camera image is received, hence about 15ms of delay can be expected on the published topics. However, the delay will be compensated for by the *"intersection_navigation"*-node.


<div figure-id="fig:4" figure-caption="Pose of the duckiebot inside a four way intersection">
    <img src="bot_in_intersection.png" style="width: 100%"/>
</div>

## Part 2: Demo and evaluation plan


### Demo plan

The proposed closed-loop intersection navigation method will be demonstrated by placing the Duckiebot at an intersection and commanding it via joystick to traverse the intersection to a desired exit (the arrows on left hand side of the joystick will be used to enter the desired exit).  The Duckiebot must be placed in a lane in front of the red stop line before executing the demo. The relative position within the lane and its orientation can vary (the initial pose must satisfy the assumption of Part 1). The demo takes as input arguments the desired exit and the navigation method, i.e. the proposed closed-loop navigation or the already existing open-loop navigation. Both arguments are optional.

In addition to the specific intersection navigation demo, the proposed closed-loop intersection navigation will be embedded in the indefinite navigation demo. The indefinite navigation demo can be run with two Duckiebots, one using the proposed closed-loop intersection navigation method and one using the existing open-loop intersection navigation method. In order to be able to distinguish the two Duckiebots, we suggest driving around with a blindfolded duck for the closed-loop method and with a duck that has its eyes wide open for the open-loop method, respectively. However, this demo will require more time to run and differences between the open-loop and closed-loop navigation (e.g. their sensitivity to the initial position at the intersection) will be harder to see.

Both demos can be run in a any Duckietown that contains at least one intersection, hence the hardware for a regular Duckietown is required (http://purl.org/dth/fall2017-map).



### Plan for formal performance evaluation

The performance of the intersection navigation is evaluated experimentally using the following measures  (in order of decreasing importance):

* Success rate, i.e. the percentage of trials for which the Duckiebot ends up in the desired lane and successfully hands over the control to the lane following controller. A trials is considered to be successful if the Duckiebot is completely inside the desired lane without touching any lane markings. The success rate is evaluated by simply performing the intersection navigation task N times and counting the number of successful trials.

* Accuracy and precision of final state, i.e. how close is the Duckiebot’s state relative to the desired final state (e.g. distance relative to the center of the lane, orientation within lane, velocity) and how repeatable is this. The accuracy and precision of final state is estimated using the already existing lane detection method, and is measured for different initial conditions.

* Accuracy and precision of estimated pose during traversing the intersection. The estimated pose will be logged and an external motion capture system, which directly outputs the pose of the Duckiebot, will be used as ground-truth.

* Duration, i.e. the average time required for the Duckiebot to cross an intersection and if possible an upper limit (worst-case) on the time required. The average duration is computed by running a series of N experiments. A (probabilistic) upper bound to navigating an intersection is found likewise.


## Part 3: Data collection, annotation, and analysis

### Collection

The use of the provided platform for data collection, annotation and analysis is not needed since we are using logs and recordings of the camera feed of Duckiebots navigating intersections.

### Annotation

No data will be annotated.

### Analysis

No dataneeds to be analyzed.
