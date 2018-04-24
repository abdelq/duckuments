#  Explicit coordination: final report {#explicit-coord-final-report status=draft}

<!--
General notes:
- REMEMBER to change the "template" in the chapter labels to your group label!
-->

## The final result {#explicit-coord-final-result}

Video of the final result:

<div figure-id="fig:explicit-coord-video">
    <figcaption> Explicit coordination's video </figcaption>
    <dtvideo src="vimeo:257762830"/>
</div>

To reproduce the results please see the [operation manual](#demo-coordination2017) .

## Mission and Scope {#explicit-coord-final-scope}

Our mission is to coordinate the intersection navigation safely and cleverly through explicit communication.

### Motivation {#explicit-coord-final-result-motivation}

Duckietowns are complex systems where the traffic situations of a real city should be emulated. These towns contain three- and four-way intersections: the Duckiebots should be able to navigate them without crashing into each other and this requires a clever coordination scheme. Intersections represent a key element of a smooth city navigation.

There are two ways of coordinating Duckiebots:
- Using a traffic light,
- Using a communication protocol between the vehicles.

Hence, we aim to have both a centralised and a decentralised solution as well as an integration of the two. While the centralised solution boils down to understand the signal emitted by a referee (i.e., a traffic light), the decentralised coordination scheme should allow the Duckiebots to operate on their own, i.e., to communicate between each other and to take decisions without any external help.


### Existing solution {#explicit-coord-final-literature}

A prior implementation for intersection coordination was already available from the 2016's MIT class. The principle was simple: When a Duckiebot comes at an intersection and  stops at the red line. Then, In the case with a traffic light, the Duckiebot detects the frequency at which the traffic light is blinking and acts based on the road rules. In the case without traffic light, the Duckiebot detects the frequency at which the other bots are blinking and adjusts its emitted frequency depending on its state. From an implementation perspective, the distinction was made a priori, i.e., the Duckiebots were not making use of the information coming from the Apriltags detection and therefore not were able to navigate systems with both types of intersection.

From the description above, we can distinguish two modules:

- LED emission and detection,
- Coordination based on the detected signals.


For the emission, three signals can be produced: each signal is encoded with a specific color and frequency. While Duckiebots are designed to recognise only frequencies, color are used to allow humans to easily understand the signals emitted by the Duckiebots. The signals represent the states: negotiation (and in which phase of the negotiation it is) or navigation of the intersection.

For the detection, the position and frequency of blinking LEDs are registered.

For the coordination, with the assumption that each vehicle can only see other vehicles on its right but not on its left, the Duckiebot yields its position if the only visible car is on the right, otherwise the Duckiebot waits (light green or red) or crosses (yellow light).



### Opportunity {#explicit-coord-final-opportunity}

The existing solution had essentially two drawbacks:

- The overall success rate was about 50%: The algorithm for LED-detection, and/or coordination failed, leading to a potential crash of the Duckiebots.
- In case of success, the LED-detection and/or coordination algorithms required an average of four minutes to clear an intersection with four Duckiebots. This results in an extremely slow process, which would block a city with dozens of Duckiebots.

Although the solution was problematic, it still gave us some important intuitions on how to solve the problem.

First of all, using a LED-communication protocol is a brilliant idea to let the Duckiebots communicate with each other. Since the previous communication algorithm had the only disadvantage of being slow (also because of several bugs), we started by re-thinking the coordination algorithm.
The existing implementation for the coordination was rather complex and articulated, resulting in confused strategies which led to the failure rate of 50%. In order to develop a simpler and lighter algorithm we took inspiration from an existing media access control protocol (MAC): the so called Carrier Sense Multiple Access (CSMA, https://en.wikipedia.org/wiki/Carrier-sense_multiple_access). This algorithm gave us the basic idea behind our strategy and allowed us to have a lighter protocol.

In the second place, we re-designed the LED-detection/-interpreter to be more efficient and robust based on the detection of blobs and not only on the detection of  frequencies.

Lastly, we wanted to have a demo that could deal with both intersections, i.e. with and without a traffic light, as opposed to the two available demos from MIT 2016's class.


## Definition of the problem {#explicit-coord-final-problem-def}

### Final objective
Given a Duckietown, Duckiebots must be able to cross an intersection efficiently.
An intersection is said to be cleared efficiently if and only if:

- The time needed to cross the intersection is below 1 minute.
- Only one Duckiebot at a time crosses the intersection.
- The Duckiebots do not crash during the navigation.

### Assumptions

####Functional assumptions

The following assumptions are made:

* The Duckiebot is of type DB17-l, i.e. has LEDs mounted on it.
* Camera works properly (frequency 30Hz, resolution 640x480)
* LEDs work properly and emit the signals with the correct color and frequency.
* Duckiebots are able to see the vehicles in front and on the right with respect to their position: one cannot assume that the left visual is clear.
* The Duckiebots do not move while “waiting” at the intersection.
* One Duckiebot navigates the intersection at the time.
* The intersection is among one of the standard intersections of Duckietown, detected through april tags.

#### Assumptions on other groups

The following assumptions are made:

* The Controllers: one to four Duckiebots are at the intersection with a certain position and orientation with respect to the stop line. Responsible for this assumption are The Controllers, which should guide the Duckiebot at intersection and make it stops with following pose:
    - Min. 0 cm behind the stop red line;
    - Max. 6 cm behind the stop red line;
    - Max. +/- (left/right deviations) 2 cm from the center of the line;
    +/- 10° of rotation with respect to the perpendicular line of the red line.
* Navigators: as soon as coordination is decided, Duckiebots have to navigate through the intersection. This task is accomplished by The Navigators.
* Implicit coordination: it is assumed that explicit and implicit coordination are never running at the same time.



### Performance metrics

The metrics that are going to be used to judge the achievement of the goal are two:

1. Mean clearing time

2. Success rate

Our goal is to work out a procedure so that the Duckiebots cross an intersection efficiently, therefore the performance metrics follow naturally.
The clearing time should not exceed one minute and the success rate should be higher than 70% in all intersection configurations (1, 2, 3 vehicles, with or without a traffic light).


## Contribution / Added functionality {#explicit-coord-final-contribution}


### LEDs Detection

LEDs are modeled as blobs in an image: A Blob is a group of connected pixels in an image that share some common properties, which, in the case of LEDs, is the intensity of the pixel. Among the many ways to detect blobs, the one that turned out to be more robust for our purpose was the following algorithm (https://www.learnopencv.com/blob-detection-using-opencv-python-c/):
- Thresholding: Convert the source images to several binary images by thresholding the source image with thresholds.
- Grouping: In each binary image, connected white pixels are grouped together.  Let’s call these binary blobs.
- Merging: The centers of the binary blobs in the binary images are computed, and blobs located closer than a threshold are merged.
- Center and Radius Calculation:  The centers and radii of the new merged blobs are computed and returned.
- Filtering: The blobs are filtered by size and shape.

To increase the robustness of the detection, a sequence of $N$ images in analyzed. Each blob $b$ is characterized with a position vector $x_b\in\mathbb{R}^2$ and a signal $y_b\in\{0,1\}^N$ of dimension, indicating whether the blob was detected in the image (1) or not (0). The blobs found are collected in a set called $B$. The algorithm works as follows:
- Initialization: Initialize the set of blobs $B$ with the empty set.
- Recursion: For image $i$ and blob $j$ (with position $x_{ij}$):
   + If $\Vert x_{ij} – x_b\Vert > \mathrm{TOL}$ for all $b\in B$ the blob is added to $B$ with $x=x_{ij}$ and $y=e_i$, where $e_i$ is a vector of dimension $N$ whose $i$ entry is 1 and all other entries are 0.
   + If $\Vert x_{ij} – x_b\Vert \leq \mathrm{TOL}$ for some $b\in B$. Then, we “merge” blob $j$ with the blob it was closest to, i.e., we set the $i$-th entry of $y_{\bar b}$ to 1, where $\bar b=\arg\min_{b\in B}\Vert x_{ij}-x_b\Vert$. That is, we store the information that the blob has been observed in the $i$-th image.

After this procedure, the user has full information about the blobs in the images. Then, one may identify the presence of another Duckiebot as follows:
- Analyzing the frequency spectrum of the signal y of each blob. If the known emission frequency and the detected frequency using the Fast Fourier Transform match, then we can conclude that a car has been detected.
- Using some heuristics. For instance, for each blob one may compute
\[
m_b=\frac{1}{N}\sum_{i=1}^N [y_b]_i
\]

and act upon this number.
This algorithms is run three times: To detect Duckiebots on the right, to detect Duckietbots on the left, and to detect traffic lights. To increase the robustness and reduce the computational demand, the image is cut accordingly. Hence, the output of the algorithm are three Booleans indicating the detection on the right, on the front, and for the traffic light respectively.  

### Coordination

Our coordination algorithm allows the hybrid management of situations with and without a traffic light.

In the situation without the traffic light, the algorithm is based on the concept of the exponential backoff, cited above. The basic concept is really simple: a Duckiebot can act on its own and decide wether to enter the intersection or to wait, without the help of a centralised system.
The Duckiebot arrives at the intersection and recognises its type. Once it stops in enters the state AT_STOP_CLEARING, which represents the action of deciding what to do. When the Duckiebot is in the state AT_STOP_CLEARING, it starts blinking at the specific defined frequency. This makes it recognisable for the potential other Duckiebots waiting in the other lanes. The other task of a Duckiebot in this state, is to check the existence other waiting Duckiebots. Since we assumed that the Duckiebot is only able to see front and right, these are the two regions of its visual where it checks if other Duckiebots are present. In order to check if a Duckiebot stays in the other lanes, we use the defined command SignalsDetection. If the Duckiebot sees other Duckiebots waiting in front or right to it, it sacrifices itself by entering in the state SACRIFICE. This consists in the first place in stopping blinking and looking, allowing other seen Duckiebots to coordinate. This state lasts for a random bounded time, defined with the variable random_delay. Once this random time has passed, the Duckiebot re-enters the state AT_STOP_CLEARING.
If instead the Duckiebot does not see any other Duckiebot waiting, it enters in the state KEEP_CALM. This state makes sure that the Duckiebot waits a different random time before deciding to navigate the interection, decreasing the chance of a possible crash due to errors in the navigation. During this period, the Duckiebot checks if other Duckiebots are blinking: if yes, he sacrifices itself and enters the state SACRIFICE; if not, it enters the state GO, which corresponds to the decision to navigate the intersection.

The coordination algorithm in the situation with the traffic light, is simpler. As the Duckiebot arrives to the intersection, it recognises its type and enters the state TL_SENSING. In this state, he checks for the traffic light signal which allows it to navigate the intersection. In this case it enters the state GO, which corresponds to the decision to navigate the intersection. If not, it waits until its turn comes.


### Logical architecture

Our job starts when Duckiebots are stationary at the red-line of the intersection (this is communicated to us via controllers/ parking).
By clicking “start” the LED-coordination-node tells the LED-emitter-node to turn the LEDs white for all Duckiebots.
Afterwards, the LED-detector-node checks for each Duckiebot if other LEDs are seen  and tells it to the LED-coordination-node. Note that here there is, at least in a first approach to the problem, no turning, i.e., LEDs of Duckiebots on the left are not identified.
The LED-coordination-node estimates the coordination move (either “hold on” or “go”) for each Duckiebot. The final output is a signal, named move_intersection, that will be used by the Navigators to start the procedure to navigate the intersection. Thereafter, we are not going to intervene until the Duckiebot finds itself at another intersection. Should the explicit coordination fail (for instance, because of Duckiebots not equipped with LEDs), the task of coordinating the intersection is given to the implicit coordination.

Our LED-detection, LED-emission and LED-coordination nodes affect only the Duckiebots behavior at intersection. Surely, our LED-signal could be seen from other Duckiebots in Duckietown but, at least for now, no group (except for the fleet planning group, see below) needs LEDs-based communication in other situations. A LED-signal will be used by fleet-planning to indicate the status of each vehicle (free, occupied, waiting, etc.). The Fleet planning will be using one LED for implementing this functionality (back-right one) while the other LEDs remain available for coordination purposes.

The following assumptions are made about other modules:


1. When the Duckiebot is made to stop at the red line by the Controllers at an intersection a flag “at_intersection” will be set and that is when the coordination will start. Most likely this flag will be sent out by the Parking group after it has been verified that after the intersection there is no parking.

2. Controllers guarantee that the Duckiebots will stop at the red line within the agreed tolerances (i.e., Min. 10cm behind center of red line;  Max. 16cm behind center of red line; +/- 10° of rotation ; +/- 5 cm offset from center of the driving lane.).

3. Fleet planning and neural-SLAM are the ones responsible to give information about where the Duckiebots should go at the intersection (information that will not be used in any case for determining how the intersection will be cleared).

4. Navigators will take over once the Duckiebot has received the order that it can proceed to navigate the intersection (a signal “go”), moment from which our team, explicit-coordination, will no longer intervene.  

5. If the Fleet planning and neural-SLAM decision is not available, the Navigators are responsible to generate a random choice for the direction that each Duckiebot will have to follow in the intersection navigation, once again, the direction that the Duckiebot will take is not of interest for the coordination part that is performed regardless of this information.

6. Explicit coordination and implicit coordination will never run at the same time on a Duckiebot.


### Software architecture

Nodes:

1. coordination_node:
    * Input: From Finite State Machine group “you are at an intersection" and apriltags detection
    * Output: Duckiebot move (“go”/ ”not go”)
    * Subscribed topic:
        * apriltags_detections from apriltags_node
        * trigger from finite state machine
    * Published topic: intersection_go
        * string message: go/no_go

2. led_emitter_node:
    * Input: Communication is needed
    * Output: LEDs turn on or stay off
    * Subscribed topic:
        * LED_switch from LED-coordination, string message: on/ off
    * Published topics: None

3. LED_detection: second option:
    * Input: camera_image (possibly after anti-instagram) and trigger
    * Output: LED detected/LED not detected with position
    * Subscribed topic:
         * Trigger from finite state machine
         * camera_image from anti-instragram, CompressedImage
    * Published topic:
         * string message: LED_detected/ no_LED_detected with position


A diagram of our nodes is shown below.


<div figure-id="fig:Nodes" figure-caption="Nodes">
     <img src="nodes.png" style='width: 80ex; height: auto'/>
</div>


We subscribe to the following topics:

* Corrected image with maximum assumed latency 1s;
* Trigger with maximum assumed latency 1s.

The following topics are published:

* Flag go/no_go with maximum latency 60s (this is the time needed to make sure that the intersection can be navigated safely).


## Formal performance evaluation / Results {#explicit-coord-final-formal}

<col4 figure-id="tab:Performance" class="labels-row1">
  <figcaption>Performance Evaluation</figcaption>

  <span>Situation</span>
  <span>Performance measure</span>
  <span>Required</span>
  <span>Obtained</span>


  <span>One Duckiebot at the intersection</span>
  <span>Clearing time</span>
  <span>60s</span>
  <span>12s</span>

  <span>One Duckiebot at the intersection</span>
  <span>Success rate</span>
  <span>90%</span>
  <span>98%</span>

  <span>Two Duckiebots at the intersection</span>
  <span>Clearing time</span>
  <span>60s</span>
  <span>25s</span>

  <span>Two Duckiebots at the intersection</span>
  <span>Success rate</span>
  <span>80%</span>
  <span>89%</span>

  <span>Three Duckiebots at the intersection</span>
  <span>Clearing time</span>
  <span>60s</span>
  <span>50s</span>

  <span>Three Duckiebot at the intersection</span>
  <span>Success rate</span>
  <span>70%</span>
  <span>89% </span>

  <span>One Duckiebot at a traffic light type intersection</span>
  <span>Clearing time</span>
  <span>60s</span>
  <span>25s </span>

  <span>One Duckiebot at a traffic light type intersection</span>
  <span>Success rate</span>
  <span>90%</span>
  <span>92% </span>
</col4>

Failures were mainly caused by the following reasons:
 - Duckiebots detecting the wrong sign (i.e., expecting a traffic light instead of a normal intersection).
 - Blobs not properly detected. This is mainly due of failures in the parameters and in the camera calibration.
 - Duckiebots crashing because of poor intersection navigation.

## Future avenues of development {#explicit-coord-final-next-steps}

There is room for improvement for the coordination part of this project.
Our approach, in the case of an intersection without traffic light, prioritises robustness rather than efficiency (in some cases all the Duckiebots at an intersection could turn off and restart the whole protocol again) and it is easy to imagine a scenario with an improved efficiency (tradeoff with complexity).

An idea would be to encode in the signal also the intentions of the Duckiebot and, by doing so, allow multiple Duckiebots to navigate the intersection at the same time if their directions are compatible. In fact, if two Duckiebots wanted to go straight they could move at the same time.
The clearing time could also be reduced in the case of an intersection with traffic light if the latter was able to see where the vehicles are (prevent the light to turn green in a direction where no vehicle is waiting to cross).
