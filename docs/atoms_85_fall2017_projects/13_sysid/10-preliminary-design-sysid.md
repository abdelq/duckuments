# System Identification: preliminary report {#sysid-pdd status=beta}


## Part 1: Mission and scope

### Mission statement

Estimate better models to make localization and control more efficient and robust to different configurations of the robot.


### Motto

Motto: NOSCE TE IPSUM <br/> (Know thyself)




### Project scope



#### What is in scope

* hardware specifications for calibration
* choose which model to "identify"
* Identify kinematic parameters (mapping of commands to actuators)
* Include model of the caster wheel

#### What is out of scope

* Additional onboard or external sensors
* Measuring the latency of the system
* Camera calibration
* State estimation using motion blur


#### Stakeholders

- Control
- localization

## Part 2: Definition of the problem

### Problem statement

Every Duckiebot is different in configuration.


> Mission = we need to make control robust to different configuration


> Problem statement = we need to identify kinematic model to make control robust enough



### Assumptions

* Robot will move only in horizontal plane
* No lateral slipping of robot
* The body fixed longitudinal velocity and angular velocity will be provided as well as the timestamp of each measurement


### Approach

* Simplified kinematic model will be used to estimate parameters for each duckiebot :
    - Semi axis length l
    - Mapping : voltage → velocity


#### Kinematic model



We make use of the no lateral slipping motion hypothesis and the pure rolling constrain as shown in the [#duckiebot-modeling](#duckiebot-modeling), to write the following equation:


\begin{align} \label{eq:mod-kin-3}
\left\{  \begin{array}{l} \dot x_A^R &= R (\dot \varphi_R +\dot \varphi_L)/2  \\
                          \dot y_A^R &= 0 \\
                          \dot \theta &= \omega = R(\dot \varphi_R - \dot \varphi_L)/(2L) \end{array} \right.,
\end{align}


Further we make the assumption that for steady state that there is a linear relationship between the input voltage and the velociy of the wheel:

\begin{align} \label{eq:mod-kin-4}
v_r=R \dot \varphi_l=c_r V_r\\
v_r=R \dot \varphi_l=c_l V_l
\end{align}

This lets us rewrite equation \eqref{eq:mod-kin-3}:

\begin{align} \label{eq:mod-kin-5}
\left\{  \begin{array}{l} \dot x_A^R &= (c_r V_r+c_l V_l)/2  \\
                          \dot y_A^R &= 0 \\
                          \dot \theta &= \omega = (c_r V_r+c_l V_l)/(2L) \end{array} \right.,
\end{align}

Using the assumption that we can measure $v_A$  we can determine $c_r$ by setting the voltage $V_l=0$.
The same procedure can be done to get $c_l$.

Using the assumption that we can measure $\dot \theta$ we will then get the semiaxis length $L$.

<div figure-id="fig:mod-kin-modeling" figure-caption="Relevant notations for modeling a differential drive robot">
  <img src="mod-kin.png" style='width: 30em; height:auto'/>
</div>

### Functionality-resources trade-offs


### Functionality provided

* A model with calibrated parameters for each duckiebot
* A calibration protocol that creates a map of:
    * input voltage → output longitudinal and angular velocity
* Semi axis length


### Resources required / dependencies / costs

* Good state estimation, independent of a model
* potential approaches for state estimate
    - lane filter
    - april tags
    - camera calibration sheet
* Accurate line-detection
* Accurate april tags



### Performance measurement

Run lane follower with old version and new version with kinematic model. Drive on the track for one minute and count the number of times the bot touches the side or center line.

**Metrics**

- Robustness to different duckies
    - Control can handle different duckiebot configurations based on our models-
- Robustness to different wheels
    - Omnidirectional wheel, caster wheel
- Robustness to initial pose
    - Run lane following using 5 different initial poses
- Repeatability
    - Run lane following 5 times and compare

We will use the performance measurement setup of the devel-control group

## Part 3: Preliminary design

### Modules and interfaces

Parameter estimation

- Input :
    - State estimation
    - Specific voltage to each wheel
- Output :
    - semi axis length and wheel radii

Mapping voltage → velocity

- Input :
    - Specific velocity to each wheel
- Output :
    - Voltage



### Preliminary plan of deliverables


### Specifications

Duckiebots with different hardware configurations for testing


### Software modules

- Parameter estimation:
    - runs calibration protocol
- Velocity translation: (Node)
    - get velocity as input and translate it to voltage as output


### Infrastructure modules

None

## Part 4: Project planning

| Date | Task Name | Target Deliverables |
|:-----------|:------------|:-------------|
| 17/11/17 | Kick-Off | Preliminary Design Document |
| 24/11/17 | Play around | Identify current problems |
| 01/12/17 | First estimation | find paramers of robot |
| 08/12/17 | Validation | Performance measure |
| 15/12/17 | Caster wheel | Performance measure of new implementation |
| 22/12/17 | Buffer | |
| 29/12/17 | Documentation | Duckuments |
| 05/01/18 | | End of Project |




### Data collection

What data do you need to collect?

### Data annotation

Performances of the current implementation


#### Relevant Duckietown resources to investigate

- Current State Estimation
- Calibration files


#### Other relevant resources to investigate

[Handbook of robotics](https://www.dropbox.com/s/0lwdwyt1a61jh0k/handbook%20of%20robotics.pdf?dl=0)

the above contains a number of interesting sections of relevance to the work of this group:

- exact modeling of caster wheel and the kinematic constraints it introduces (pg. 395)

- different system identification procedures: parametric or nonparametric (Chapter 14); in particular, a note on Observability (pg. 337)

- we want to maximize performance of control + localization. Control uses unicycle model in Frenet frame (pg. 803 of handbook of robotics)

- We need to identify wheel radii (r_1, r_2: assume equal at start = r), semi-axle length L, and motors steady state parameters (mapping between voltage and angular rate, i.e. mapping between voltage and velocity once (a) wheel radius is known and no slipping hypothesis is made).

- Adaptive control (pg. 147): another approach is implementing an adaptive controller. It is  meant to work with plant uncertainty.

[Caster wheel literature](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0FB474602C01DDB0FAA1B5C68DB8245E/S026357470001883Xa.pdf/div-class-title-modeling-and-path-tracking-control-of-a-mobile-wheeled-robot-with-a-differential-drive-div.pdf)




### Risk analysis

What could go wrong?

- It could happen that we identify a model which is not useful for control.
- Perfect model will be useless if control is not improved

Mitigation strategy:

- Early testing with control group
