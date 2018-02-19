#  System identification: final report {#sysid-final-report status=draft}


## The final result {#sysid-final-result}

<div figure-id="fig:demo_succeeded-sysid">
    <figcaption>Demo of the calibration procedure
    </figcaption>
    <dtvideo src='vimeo:251027149'/>
</div>

To reproduce the results see the  [operation manual](#demo-sysid) which includes detailed instructions for a demo.


## Mission and Scope {#sysid-final-scope}

### Motivation {#sysid-final-result-motivation}

The mission is to make the controller more robust to different configurations of the robot. The approach chosen to do this is obtaining a mathematical model of the Duckiebot in order to understand its behavior. The mathematical model can then be used to design a controller to obtain robust desired behaviors and performances.

The Duckiebot is in a differential-drive configuration. It actuates each wheel with a separate DC Motor. By applying the same torque on both wheels one can go straight, and by applying different torques the Duckiebot turns. A schematic overview of the model can be seen in Figure [](#fig:model) [](#bib:Modeling).

<div figure-id="fig:model" figure-caption="Model of differential drive robot">
  <img src="model.PNG" style='width: 30em; height:auto'/>
</div>

A model for a differential drive robot is derived in section in chapter [#duckiebot-modeling](#duckiebot-modeling). This model can be used to provide a simple method of maintaining an individual’s position or velocity estimate in the absence of computationally expensive position updates from external sources such as the mounted camera.

The derived non-linear model describes the expected output of the pose (e.g. position, velocity) w.r.t. a fixed inertial frame for a certain voltage input. The model makes several assumptions, such as rigid body motion, symmetry, pure rolling and no lateral slipping.

Most important of all, the model assumes the knowledge of certain constants that characterize the DC motors as well as the robot’s geometry.

However, there will never be two duckiebots that show exactly the same behavior. This can be very problematic. 
You might have noticed that your vehicle doesn’t really go in a straight line when you command it to. 
For example, when the same voltage is supplied to each motor, the Duckiebot will not go straight as might expected. 
Also, the vehicle might not go at the velocity you are commanding it to drive at.
Therefore, these constants needs to be identified individually for each single robot. The determination process to do so is called system identification. 
Odometry calibration is the process of determining model parameter to “match” predicted motion and measurements. For the duckiebot odometry calibration is the process aimed at identifying the kinematic parameters used to reconstruct the robot’s absolute configuration from the given voltage input. 

Increasing the accuracy of the Duckiebot’s odometry will result in reduced operation cost as the robot requires fewer absolute positioning updates with the camera.
When the duckiebot crossing an intersection forward kinematics is used. 
Therefore, the performance of safe crossing is closely related to having well calibrated odometry parameters.


### Existing solution {#sysid-final-literature}


#### Forward Kinematics

The existing model was the following : 

\begin{align}
    V_{l} &= (g+t)(v_{A}-\omega L)  \label{eq:V_l}     \\
    V_{r} &= (g-t)(v_{A}+\omega L)  \label{eq:V_r}
\end{align}


<div markdown="1">

 <col2 id='sysid-notations2' figure-id="tab:sysid-notations2" figure-caption="Notations for odometry calibration a differential drive robot">
    <s>$V_{l,r}$</s>  <s>Voltage to left/right motors</s>
    <s>$g$</s>  <s>Gain</s>
    <s>$t$</s>  <s>Trim</s>
    <s>$v_{A}$</s>  <s>Linear velocity of Duckiebot in bodyframe</s>
    <s>$\omega$</s>  <s>Angular velocity</s>
    <s>$L$</s>  <s>Half of distance between the two wheels</s>
 </col2>
 
</div>


Note that if the gain $g = 1.0$ and trim $t= 0.0$, the wheel’s voltages are exactly the same as the linear velocity + or - angular velocity times half the baseline length $V_{l,r}=v_a \pm \omega L$.
With gain $g > 1.0$ the vehicle goes faster given the same velocity command, and for gain $g < 1.0$ it would go slower.
With trim $t > 0$, the right wheel will turn slightly more than the left wheel given the same velocity command; with trim $t<0$, the left wheel will turn slightly more the right wheel.

The parameters $g$ and $t$ were to be set manually during the wheels calibration procedure.  

#### Existing Calibration Procedure

The current implementation of the calibration procedure can be found in the [#wheel-calibration](#wheel-calibration) section.

Hereby, the Duckiebot is placed on a line(e.g. tape). Afterwards the joystick demo is launched with the following command:

    duckiebot: $ roslaunch duckietown_demos joystick.launch veh:=${VEHICLE_NAME}

Now the human operator commands the Duckiebot to go straight for around 2m.

Observe the Duckiebot from the point where it started moving and annotate on which side of the tape
the Duckiebot drifted ([](#fig:wheel_calibration_lr_drift)).


<div figure-id="fig:wheel_calibration_lr_drift" figure-caption="Left/Right drift">
  <img src="wheel_calibration_lr_drift.jpg" style='width: 30em'/>
</div>

If the Duckiebot drifted to the left side of the tape, decrease the value of $t$, for example:


    duckiebot: $ rosservice call /${VEHICLE_NAME}/inverse_kinematics_node/set_trim -- 0.01

Or Changing the trim in a negative way, e.g. to -0.01:

    duckiebot: $ rosservice call /${VEHICLE_NAME}/inverse_kinematics_node/set_trim -- -0.01

This procedure is repeated until there is less than around $10 cm$ drift for two meters distance.
The speed of the duckiebot can be adjusted by setting the gain:

    duckiebot: $ rosservice call /${VEHICLE_NAME}/inverse_kinematics_node/set_gain -- 1.1

The parameters of the Duckiebot are saved in the duckietown/config/baseline/calibration/kinematics/{VEHICLE_NAME}.yaml file.

### Opportunity {#sysid-final-opportunity}

#### Current shortcomings
* Human in the loop
    * The car is not able to calibrate itself without human input
    * The procedure is laborious and can be long
* Lack of precision
    * The calibration is only done for a straight line
    * The speed of the Duckiebot is not known



#### Possible approaches

A crucial step should be to take the human out of the loop.
This means that the car will calibrate itself, without any human input.

There were several possible approaches discussed to overcome the shortcomings of the current calibration:

* Localization based calibration
    * E.g. determine relative pose w.r.t. Chessboard from successive images
* Closed loop calibration
    * Modify the trim while Duckiebot is following a loop until satisfactory
* Motion blur based calibration
    * Reconstruct dynamics from blurred images

Because we needed to have very precise measurments of the Duckiebot's position, the localization based calibration has been chosen. To simplify the calibration procedures, we decided also to use the same chessboard as for the camera calibration.
But since the computational power needed for detecting the chessboard was big, we chose to do the chessboard detection on the laptop.

We also kept a kynematic model, without including any dynamic and made some assumptions about the physics of the Duckiebot: the wheels do not slip and the velocity of the wheels is proportional to the voltage applied. 
Hence, if the results do not meet our expectations or if the Duckiebot is changed, the model can aslo be changed or it can be made more complex. 


### Preliminaries {#sysid-final-preliminaries}

* Differential-drive model [#duckiebot-modeling](#duckiebot-modeling)
    
* Pinhole-camera model [#camera-geometry](#camera-geometry)



## Definition of the problem {#sysid-final-problem-def}

The approach we chose to imporve the behaviour of the Duckiebots was to derive a model with some parameters, and to identify this parameters for each Duckiebot independantely. 
Hence, we first construct a model and then we try to fit the model to the measurement we get.



### Kinematic model 

The Duckiebot was modeled as a symmetric rigid body, according to the following figure. 

<div figure-id="fig:mod-kin" figure-caption="Schematics of differential drive robot [](#bib:Modeling)">
  <img src="mod-kin.png" style='width: 30em; height:auto'/>
</div>
	
Hence, Considering only the kinematics, we get the following equations for the linear and angular velocity $v_A $ and $\dot{\theta}$ of the Duckiebot : 
	
\begin{eqnarray}
	 v_A &= \cfrac{v_r + v_l}{2}
	 \label{vA} \\
	 \dot{\theta} &= \cfrac{v_r - v_l}{2L}
	\label{theta}
\end{eqnarray} \\ 


 With the assumption that the velocity of the wheels is proportional to the voltage applied on each wheel $V_l$ and $V_r$ and that there is no slipping,  we can write the following : 

\begin{eqnarray}
	 v_l &= c_l \cdot V_l
	  \label{vl} \\ 
	 v_r &= c_r \cdot V_r
	\label{vr}
\end{eqnarray}

 Thus ~\eqref{vA} and ~\eqref{theta} can bre rewritten as : 

\begin{eqnarray}
	v_A &= \cfrac{c_r \cdot V_r + c_l \cdot V_l }{2}
	 \label{vA2} \\ 
	\dot{\theta} &= \cfrac{c_r \cdot V_r - c_l \cdot V_l }{2L}
	 \label{theta2}
 \end{eqnarray}

With, $c_r, c_l $ and $L$, some constants to define for each duckiebot. \\ \\ 


Alternatively, we can define $c = c_r$ and $c_l = c + \Delta c$ and we get from  ~\eqref{vA3} and ~\eqref{theta3} 

\begin{eqnarray}
	v_A &= \cfrac{c \cdot (V_r +  V_l ) + \Delta c \cdot V_l}{2}
	\label{vA3} \\ 
	\dot{\theta} &= \cfrac{c \cdot (V_r - V_l ) - \Delta c \cdot V_l}{2L}
	\label{theta3}
 \end{eqnarray}

We get a kinematic model, that shows the relation between the linear and angular velocity of the Duckiebot and the voltage applied to each wheel. To have our model totally defined, we only need to calculate three parameters, namely $c $ and $\Delta c$ and $L$. 
These three parameters will be calculated with odometry calibration.


### Odometry formulation {#sysid-final-odometry}

The general problem definition for the odometry is to find the most likely calibration parameters given the duckiebot model [#duckiebot-modeling](#duckiebot-modeling) and a set of discrete measurement from which the output can be estimated. [](#bib:OdometryCalibration) 
The model of the system [](#bib:OdometryCalibration) with the notations explained in Table [](#tab:sysid-notations) can be described as :

\begin{align}
    \dot{x} &= f(p;x,u)       \label{eq:model1} \\
      y & = g(x)       \label{eq:model2} \\
      \mathcal{M}_{n} & = \{ m_k=m(t_k), t_1 < \dots < t_k < \dots < t_n)\}     \label{eq:measurements} \\
      \hat{\mathcal{Y}}_{n} & = \{ \hat{y}_{k}=h(m_k),k=1, \dots ,n \}             \label{eq:outputestimates}
\end{align}


<div markdown="1">
 <col2 id='sysid-notations1' figure-id="tab:sysid-notations1" figure-caption="Notations for odometry calibration a differential drive robot">
    <s>$p$</s>  <s>Calibration Parameters</s>
    <s>$f(\cdot)$</s>  <s>Model </s>
    <s>$g(\cdot)$</s>  <s>Pose </s>
    <s>$\mathcal{M}_{n}$</s>  <s>Set of discrete measurements</s>
    <s>$m_k$</s>  <s>Measurements (not necessarily evenly space in time)</s>
    <s>$\hat{\mathcal{Y}}_{n}$</s>  <s>Set of output estimates</s>

 </col2>
</div>


The model $f(\cdot)$ can be a kinematic model, constrained dynamic model or more general dynamic model.
The pose $g(\cdot)$ can be the robot pose or the sensor pose.
The measurements $m_k$ can be from "internal" sensors e.g. wheel encoders, IMUs etc. or from "external" sensors such as Lidar, Infrared or camera.


For our project, our set of measurments was obtained thanks to the camera : we put the Duckiebot in front of a chessboard, and then we were able to derived the position of the Duckiebot at every image relative to the chessboard. 

At the same time, from our kinematic model, we could estimate the position of the Duckiebot $\big( x_i, y_i\big) $ recursively with the formula : 


\begin{align}
    x_{k+1} & = x_k+v_A \cdot cos(\theta)  \label{eq:1}     \\
    y_{k+1} & = y_k+v_A \cdot sin(\theta)  \label{eq:2}
\end{align}

Because $v_A=\frac{c_r \cdot V_r+c_l \cdot V_l}{2}$ we can express every position $x_i,y_i$ of the Duckiebot with help of the parameters:

\begin{align}
    x_{k+1} & = x_k+\frac{c_r \cdot V_r+c_l \cdot V_l}{2} \cdot cos(\theta)  \label{eq:xk}     \\
    y_{k+1} & = y_k+\frac{c_r \cdot V_r+c_l \cdot V_l}{2} \cdot sin(\theta)  \label{eq:yk}
\end{align}

By minimizing the position of the Duckiebot $x_i,y_i$ and its theoretical position given by our model $x_i,y_i$ at every time $t_i$ , we can estimate the parameters $c_r , c_l$ and $L$.

We used the L2-norm :

\begin{equation}
    \begin{pmatrix}c_{l}^{\star}\\c_{r}^{\star}\\L^{\star}\end{pmatrix}= \underset{c_l,c_r,L}{\mathrm{argmin}}   \begin{pmatrix} x_1-\tilde{x}_1\\y_1-\tilde{y}_1\\\vdots\\x_n-\tilde{x}_n\\y_n-\tilde{y}_n\end{pmatrix}^T  \begin{pmatrix} x_1-\tilde{x}_1\\y_1-\tilde{y}_1\\\vdots\\x_n-\tilde{x}_n\\y_n-\tilde{y}_n\end{pmatrix}
    
\end{equation}


### Dealing with uncertainty

Because our model does not take into account the dynamics of the system, and many assumptions as been made, the results we will get won’t perfectly match with the reality.
Assuming that the states estimation $v_{a_{i}}$ and $\dot{\theta}_{i}$ is accurate enough
and a Gaussian distribution of the noise, we can quantify this nose by estimating its variance :


\begin{align}
    \sigma_v^2 & = \frac{1}{n}  \sum_{k=1}^n (v_{A_{i}}-\tilde{v}_{A_{i}})^2  \label{eq:sigmav}     \\
    \sigma_{\dot{\theta}}^2 & = \frac{1}{n}  \sum_{k=1}^n (\dot{\theta}_{A_{i}}-\tilde{\dot{\theta}}_{A_{i}})^2   \label{eq:sigmatheta}
\end{align}

with 

\begin{align}
    \tilde{v}_{A_{i}} & = \frac{c_{r}^{\star} V_{r_i}+c_{l}^{\star} V_{l_i}}{2} \label{eq:vtilde}     \\
    \tilde{\dot{\theta}}_{A_{i}} & = \frac{c_{r}^{\star} V_{r_i}-c_{l}^{\star} V_{l_i}}{2L^{\star}}   \label{eq:thetatilde}
\end{align}




## Contribution / Added functionality {#sysid-final-contribution}

The calibration procedure consists of two parts:

* Recording rosbag for different duckiebot maneuvers in front of chess board

* Offline processing of rosbag to find odometry parameters with fit

To reproduce the results see the  [operation manual](#demo-sysid) which includes detailed instructions for a demo.

### Recording rosbag log of Duckiebot maneuvers

Place the Duckiebot in front of the chessboard at a distance of slightly more than 1 meter in front of the checkerboard (~2 duckie tiles), as shown in the image ().. The heading has to be set iteratively to maximize the time the duckiebot sees the checkerboard.

<div figure-id="fig:calibration_setup" figure-caption="The calibration setup">
     <img src="calibration_setup.jpg" style='width: 30em'/>
</div>

Run the calibration procedure

    duckiebot $ roslaunch calibration commands.launch veh:=robot name

The Duckietown should go forward and then stop. 

Step 5 When the Duckiebot has stopped, you have 10 seconds to replace it again at a distance of approximately 1 meters of the chessboard. Wait for the Duckiebot to move forward again.


Step 8: Run the calibration process with 

    laptop $ roslaunch calibration calibration.launch veh:=robot name  path:=/absolute/path/to/the/rosbag/folder/
    
(path example: path:=/home/user_name/sysid/) Do not forget the backslash at the end of the path.(Common mistake: path not starting from /home, forgetting the last / in the path)

Step 9: Once the command has finished, the parameters of your Duckiebot are stored in the folder

    ![DUCKIEFLEET_ROOT]/calibrations/kinematics/![robot name].yaml
    
Step 10: Push the duckiefleet changes to git and pull from the duckiebot






### Pose estimation w.r.t. chessboard


#### Step 1 - Find 2D image points of chessboard in picture

To to find pattern in chess board, we use the function, [findChessboardCorners](https://docs.opencv.org/3.0-beta/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html#drawchessboardcorners "OpenCV findChessboardCorners")
It gives us the image points locations where two black squares touch each other in chess boards)

We also need to pass what kind of pattern we are looking, like 8x8 grid, 5x5 grid etc. For duckietown, we use 7x5 grid. (Normally a chess board has 8x8 squares and 7x7 internal corners).
It returns the corner points and retval which will be True if pattern is obtained.
These corners will be placed in an order (from left-to-right, top-to-bottom).

In order that the chessboard detection works reliable, one need an assymetric pattern. (e.g. [here](https://github.com/opencv/opencv/blob/3.3.1/doc/pattern.png)).
However, the standard chessboard provided by Duckietown includes an ambiguity, i.e. if the chessboard looks the same if chessboard image is turned 180 degrees.
This can result in the issue that the [findChessboardCorners](https://docs.opencv.org/3.0-beta/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html#drawchessboardcorners "OpenCV findChessboardCorners") functions from right-to-left, bottom-to-top.
Therefore, the origin of chessboard coordinate frame switches from the upper-left to the lower-right corners for certain images.
A fix is implemented to overcome this inconsistency in order to make it work for the default Duckietown chessboard.
However it is suggested to use an assymmetric chessboard for future use, or a [ChArUco Board](https://docs.opencv.org/3.1.0/df/d4a/tutorial_charuco_detection.html). 

If the chessboard is successfully found in the image, the corners position are refined with the [cv2.cornerSubPix()](https://docs.opencv.org/3.0-beta/modules/imgproc/doc/feature_detection.html#cornersubpix "OpenCV cornerSubPix()") function.

The chessboard is then projected on to the image for debugging purposes [](#fig:DrawChessboard).

<div figure-id="fig:DrawChessboard" figure-caption="Projected chessboard">
  <img src="DrawChessboard.png" style='width: 30em'/>
</div>

 
#### Step 2 - Find the rotation and translation vectors of chessboard w.r.t camera 

The next steps is to find the relation between the found image points and the objects points, the so called extrensic parameters.
Extrinsic parameters corresponds to rotation and translation vectors which translates a coordinates of a 3D point to a coordinate system.
3D points are called object points and 2D image points are called image points.

The chessboard was kept stationary at XY plane, (so $Z=0$ always) and camera was moved accordingly. This consideration helps us to find only $X$,$Y$ values. Now for $X$,$Y$ values, we can simply pass the points as $(0,0), (1,0), (2,0), ...$ which denotes the location of points. In this case, the results we get will be in the scale of size of chess board square. But if we know the square size, (Duckie chessboard $32 mm$), and we can pass in our case the values as $(0,0),(32,0),(64,0),...,$ we get the results in mm. 

For the pose estimation we need to know the extrinsic and extrinsic parameters of the camera.
They can be loaded with the implemented load_camera_info() duckietown function.
Intrinsic parameters are specific to a camera. It includes information like focal length ($f_x$,$f_y$), optical centers ($c_x$,$c_y$) etc. It is also called camera matrix. It is expressed as a 3x3 matrix:


\begin{equation}
    camera \; matrix = \left [ \begin{matrix} f_x & 0 & c_x \\ 0 & f_y & c_y \\ 0 & 0 & 1 \end{matrix} \right ]
\end{equation}


We are using the function cv.solvePnPRansac() to calculate the rotation and translation. [solvePnPRansac](https://docs.opencv.org/3.0-beta/modules/calib3d/doc/camera_calibration_and_3d_reconstruction.html#solvepnpransac "OpenCV solvePnPRansac") finds an object pose from 3D-2D point correspondences using the RANSAC scheme.
It uses the object points, the chessboard corners and the camera matix as an input and gives the translation $t_{CamChess}$ and rotation $R^{Cam}_{Chess}$

#### Step 3 - Find the rotation and translation vectors of duckiebot w.r.t chessboard

We are interested to find the vehicle pose with respect to world frame. 
This is done by using the homography relation:

\begin{equation}
                       T^{I}_{cam}=T^{I}_{chess} T^{chess}_{cam}
\end{equation}

where as we use the following equations:

\begin{align}
    T^{world}_{veh} & = \begin{bmatrix}R^{I}_{veh}&t_{I  Veh}\\0&1\end{bmatrix}     \label{eq:world} \\
                    & = \begin{bmatrix}R^{chess}_{cam}&t_{ChessCam}\\0&1\end{bmatrix}     \label{eq:world1} \\
                    & = \begin{bmatrix}(R^{cam}_{chess})^T&-(R^{cam}_{chess})^T t_{CamChess}\\0&1\end{bmatrix} \label{eq:world2} 
\end{align}


The yaw $\theta$ can then be extracted from $R^{I}_{veh}$ with the implemented rot2euler() function.
The resulting translation can be extracted from $t_{I Veh}$



### Extract Duckiebot pose w.r.t chessboard from successive image recorded in rosbag




### Fit




## Formal performance evaluation / Results {#sysid-final-formal}

### Plan for Performance evaluation

** Pose estimation w.r.t. chessboard from successive images**  :


Run the Validation: Duckiebot should first drive straight for 1m (in 5s) then turn a full circle to the left (in 8s) and then a full circle to the right (in 8s)

    duckiebot $ roslaunch calibration test.launch

known issue: the baseline is rather overestimated at the moment, thus the duckiebot will probably turn more than a circle

** Offset in straight line **  :

We will let the Duckiebot drive straight in open loop and measure its offset after X tiles of straight lane in Duckietown. The performance metric will be the absolute position offset of the expected to the actual terminal position after the run, measured with a ruler.

** Circle test ** : 

We will will drive the Duckiebot with a constant velocity $ v_a $ and constant angular velocity $ \dot \omega $ in open loop on a Duckietown corner tile. We will compare the actual path with the desired path. This is done both clock and counterclockwise. The performance metric will be the absolute position offset of the expected to the actual terminal position after the run, measured with a ruler.

** Overall User friendliness ** : 

<div figure-id="fig:demo">
    <figcaption>Demo of the calibration procedure
    </figcaption>
    <dtvideo src='vimeo:251383652'/>
</div>



The current calibration is done offline. USB stick etc. 
Of course, this can be improved in future efforts.=> Future make online



** Integration test  **
show that intersection crossing is more reliable with sysid


When the duckiebot crossing an intersection forward kinematics is used. 
Therefore, the performance of safe crossing is closely related to having well calibrated odometry parameters.


## Future avenues of development {#sysid-final-next-steps}

* Simultaneous odometry and camera calibration

* Position estimation based on april tags

* Caster wheel identification
    * Initial aim was to include the kinematics of the caster wheel, however due to time constraint, we sticked to the roller wheel
    
* Dynamic model of the Duckiebot
