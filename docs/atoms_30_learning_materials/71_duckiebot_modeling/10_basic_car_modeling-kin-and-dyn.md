# Duckiebot modeling {#duckiebot-modeling status=beta}

Obtaining a mathematical model of the Duckiebot is important in order to (a) understand its behavior and (b) design a controller to obtain desired behaviors and performances, robustly.

The Duckiebot uses an actuator (DC motor) for each wheel. By applying different torques to the wheels a Duckiebot can turn, go straight (same torque to both wheels) or stay still (no torque to both wheels). This driving configuration is referred to as _differential drive_.

In this section we will derive the model of a differential drive wheeled robot. The Duckiebot model will receive voltages as input (to the DC motors) and produce a configuration, or pose, as output. The pose describes unequivocally the position and orientation of the Duckiebot with respect to some Newtonian "world" frame.

<!--, and finally describe procedures for odometry calibration, i.e., the determination of those of parameters necessary to particularize the general model to each specific Duckiebot.-->

Different methods can be followed to obtain the Duckiebot model, namely the Lagrangian or Newton-Euler, we choose to describe the latter as it arguably provides a clearer physical insight. Showing the equivalence of these formulations is an interesting exercises that the interested reader can take as a challenge. A useful resource for modeling of a Duckiebot may be found here [](#bib:desantis1995modeling).

<div class='requirements' markdown="1">

Requires:[k:reference_frames](#reference_frames) (inertial, body), [k:intro-transformations](#transformations) (Cartesian, polar)

Requires: [k:intro-kinematics](#intro-kinematics)

Requires: [k:intro-dynamics](#intro-dynamics)

Suggested: [k:intro-ODEs-to-LTIsys](#intro-ode2lti)

Result: k:diff-drive-robot-model

</div>

## Preliminaries {#mod-prelim}

TODO: relabel inertial frame -> local frame; $(\cdot)^I \rightarrow (\cdot)^L$

We first briefly recapitulate on the [reference frames](#reference-frames) that we will use to model the Duckiebot, with the intent of introducing the notation used throughout this chapter. It is important to note that we restrict the current analysis to the plane, so all of the following in defined in $\reals^2$.

To describe the behavior of a Duckiebot three reference frames will be used:

- A "_world_" frame: a right handed fixed reference system with origin in some arbitrary point $O$. We will indicate variables expressed in this frame with a superscript $W$, e.g., $X^W$, unless there is no risk of ambiguity, in which case no superscript will be used.

- An "_inertial_" frame: a fixed reference system parallel to the "world" frame, that spans the plane on which the Duckiebot moves. We will denote its axis as $\{X_I, Y_I\}$, and it will have origin in point $A=(x_A, y_A)$, i.e., the midpoint of the robot's wheel axle. We will indicate variables expressed in this frame with a superscript $I$, e.g., $X^I$, unless there is no risk of ambiguity, in which case no superscript will be used.

- A _body_ (or "robot") frame: a local reference frame fixed with respect to the robot, centered in $A$ as well. The $x$ axis points in the direction of the front of the robot, and the $y$ axis lies along the axis between the wheels, so to form a right handed reference system. We denote the robot body frame with $\{X_R, X_R\}$. The same superscript convention as above will be used. The wheels will have radius $R$.

Note: The robot is assumed to be a rigid body, symmetric, and $X_r$ coincides with axis of symmetry. Moreover, the wheels are considered identical and at the same distance, $L$, from the axle midpoint $A$.

Moreover:

- The center of mass $C^W = (x_c, y_c)$ of the robot is on the $x_r$ axis, at a distance $c$ from $A$, i.e., ($C^R = (c, 0)$);

- $X^r$ forms an _orientation angle_ $\theta$ with the local horizontal plane.

These notations are summarized in [](#fig:mod-kin).

<div figure-id="fig:mod-kin" figure-caption="Relevant notations for modeling a differential drive robot">
  <img src="mod-kin.png" style='width: 30em; height:auto'/>
</div>

### Moving between frames

We briefly recapitulate on a few transformations that we will use throughout this chapter.

#### Translations

Let $\avec{x^I} = [x^I, y^I]$ be a vector represented in the inertial frame and $\avec{X^I} = [x^I, y^I, 1]^T$ be its augmented version. It is possible to express such vector in the world frame through a translation:

\begin{align} \label{eq:mod-translation-i2w}
\avec{X^W}= \amat{T}\avec{X^R},
\end{align}

where the translation matrix $\amat{T}$ is defined as:

\begin{align}
\amat{T} = \left[  \begin{array}{ccc} 1 & 0 & x_A  \\ 0 & 1 & y_A \\ 0 & 0 & 1 \end{array} \right] \left[\begin{array}{c} x^I  \\ y^I \\ 1 \end{array} \right].
\end{align}

In the Euclidian space, each translation preserves distances (norms), i.e., is an isometry. So, for example, a velocity expressed in the inertial frame will have the same magnitude as that velocity expressed in the world frame.

#### Rotations

Let $\avec{x^R} = [x^R, y^R]^T$ be a vector represented in the robot frame and $\avec{X^R} = [x^R, y^R, 1]^T$ its augmented version. It is possible to express such vector in the inertial frame through a rotation:

\begin{align} \label{eq:mod-rotation-r2i}
\avec{X^I}= \amat{R}(\theta)\avec{X^R},
\end{align}

<!--
\begin{align} \label{eq:mod-r2i}
\left[\begin{array}{c} x^I \\ y^I \\ 1 \end{array} \right] = \left[  \begin{array}{ccc} \\cos\theta & -\sin \theta  & 0 \\ \\sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{array} \right] \left[\begin{array}{c} x^R \\ y^R \\ 1 \end{array} \right]= \amat{R}(\theta)\avec{x^R}.
\end{align}
-->

where $\amat{R}(\theta) \in SO(2)$ is an orthogonal rotation matrix:

\begin{align} \label{eq:mod-rot-mat}
\amat{R}(\theta) = \left[  \begin{array}{ccc} \cos\theta & -\sin \theta  & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{array} \right].
\end{align}

<!--
\begin{align} \label{eq:mod-rot-mat2}
\amat{R}(\theta) = \left[  \begin{array}{ccc} \\cos\theta & -\sin \theta  & 0 \\ \\sin\theta & \cos\theta & 0 \\ x_A & y_y & 1 \end{array} \right].
\end{align}
-->

Note: The orthogonality condition implies that $\amat{R}^T(\theta)\amat{R}(\theta) = \amat{R}(\theta)\amat{R}^T(\theta) = \amat{I}$, hence:
$$
\label{eq:mod-orthogonality-cond}
\amat{R}^T(\theta) = \amat{R}^{-1}(\theta),
$$
which is quite nice.

#### Roto-translation

A corollary of \eqref{eq:mod-translation-i2w} and \eqref{eq:mod-rotation-r2i} is that the translations and rotations can be combined in a single transformation, because $\avec{X^W} = \amat{T}\avec{X^I} = \amat{T} \amat{R}(\theta)\avec{X^R}$. The combined transformation matrix is given by:

\begin{align} \label{eq:mod-rototranslation-mat}
\amat{T} \amat{R}(\theta) = \left[  \begin{array}{ccc} \cos\theta & -\sin \theta  & x_A \\sin\theta & \cos\theta & y_A \\ 0 & 0 & 1 \end{array} \right].
\end{align}

<!--
The position of the robot with respect to the inertial frame is completely characterized by:

\begin{align}
\avec{q^I} = \left(  \begin{array}{c} x_A  \\ y_A \\ \theta \end{array} \right),
\end{align}

and it is always possible to switch representation of a vector $X$ from the robot to inertial frames through:
-->

## Dynamics


While kinematics studies the properties of motions of geometric (i.e., massless) points, dynamical modeling takes into account the actual material distribution of the system. Once mass comes into play, motion is the result of the equilibrium of external forces and torques with inertial reactions. While different approaches can be used to derive these equations, namely the Lagrangian or Newtonian approaches (former based on energy considerations, latter on equilibrium of generalized forces), we choose to follow the Newtonian one here for it grants, arguably, a more explicit physical intuition of the problem. Obviously both methods lead to the same results when the same hypothesis are made.

### Notations {#mod-dyn-notations}

For starters, recalling that $C^r = (c, 0)$ is the center of mass of the robot, we define the relevant notations:

<div markdown="1">

 <col2 id='mod-dyn-notations' figure-id="tab:mod-dyn-notations" figure-caption="Notations for dynamic modeling of a differential drive robot">
    <s>$(v_u, v_w)$</s>  <s>Longitudinal and lateral velocities of $C$, robot frame</s>
    <s>$(a_u, a_w)$</s>  <s>Longitudinal and lateral accelerations of $C$, robot frame</s>
    <s>$(F_{u_R}, F_{u_L})$</s>  <s>Longitudinal forces exerted on the vehicle by the right and left wheels</s>
    <s>$(F_{w_R}, F_{w_L})$</s>  <s>Lateral forces exerted on the vehicle by the right and left wheels</s>
      <s>$(\tau_R, \tau_L)$</s>  <s>Torques acting on right and left wheel</s>
    <s>$\theta$, $\omega = \dot \theta$</s>  <s>Vehicle orientation and angular velocity</s>
    <s>$M$</s>  <s>Vehicle mass</s>
    <s>$J$</s>  <s>Vehicle yaw moment of inertia with respect to the center of mass $C$</s>
 </col2>

</div>

[](#fig:mod-dyn) summarizes these notations.

Before deriving the dynamic model of the robot, it is useful to recall some elements of polar coordinates kinematics.

### Polar coordinates kinematics

Let $\avec{r}(t)$ identify a point in the space from the inertial frame at distance $r(t)$ from the $A$.

Warning: You might want to refresh [Euler formula](https://en.wikipedia.org/wiki/Euler%27s_formula) to convince yourself about the following.

\begin{align} \label{eq:mod-polar-kin-deriv}
\avec{r}(t) &= r(t) e^{j\theta(t)} \\
\avec{\dot r}(t) &= v_u(t) e^{j\theta(t)} + v_w(t) e^{j(\theta(t)+\frac{\pi}{2})} \\
\avec{\ddot r}(t) &= a_u(t) e^{j\theta(t)} + a_w(t) e^{j(\theta(t)+\frac{\pi}{2})},
\end{align}

with:

\begin{align} \label{eq:mod-polar-kin-coeff}
v_u(t) &= \dot r(t)\\
v_w(t) &= r (t) \dot \theta (t)\\
a_u(t) &= \dot v_u - v_w \dot \theta (t) = \ddot r(t) - r \dot \theta^2(t)\\
a_w(t) &= \dot v_w + v_u \dot \theta (t) = 2 \dot r (t) \dot \theta (t) + r(t) \ddot \theta (t).
\end{align}

Keeping \eqref{eq:mod-polar-kin-deriv} and \eqref{eq:mod-polar-kin-coeff} in mind, it is useful to note (for later use) that, letting $\avec{r}(t)$ identify the position of the center of mass $C$ in the inertial frame:

\begin{align} \label{eq:mod-C-world-pos}
\left\{  \begin{array}{ll} x_C^W(t) &= x_A(t) + r(t) \cos\theta(t) \\
                          y_C^W(t) &= y_A(t) + r(t) \sin\theta(t)   \end{array} \right.,
\end{align}

and therefore:

\begin{align} \label{eq:mod-A-dot-polar}
\left\{  \begin{array}{ll} \dot x^I_A(t) &= x^W_C(t) - v_u(t) \cos\theta(t) + v_w(t) \sin\theta(t)\\
                          \dot y^I_A(t) &= y^W_C(t) - v_u(t) \sin\theta(t) - v_w(t) \cos\theta(t)   \end{array} \right..
\end{align}

### Free body diagram {#mod-dyn-fbd}

The next step, and definitely the most critical, is writing the free body diagram of the problem ([](#fig:mod-dyn)). In this analysis the only forces acting on the robot are those applied from the wheels to the vehicle's chassis. It is important to note that the third passive wheel (omnidirectional or caster) is not being taken into account.

<div figure-id="fig:mod-dyn" figure-caption="Free body diagram of a differential drive robot">
  <img src="mod-dyn.png" style='width: 30em; height:auto'/>
</div>

### Equilibrium of forces and moments {#mod-dyn-eq}

We derive the dynamic model by imposing the simultaneous equilibrium of forces along the longitudinal and lateral directions in the robot frame with the respective inertial forces, and of the moments around the vertical axis (coming out of the.. screen) passing through the center of mass of the robotic vehicle.

\begin{align} \label{eq:mod-dyn-equilibria}
Ma_u(t) &= F_{u_L}+F_{u_R} \\
Ma_w(t) &= F_{w_L}+F_{w_R} \\
\ddot{\theta}(t) &= \frac{L}{J}(F_{u_R}-F_{u_L}) + \frac{c}{J}(F_{w_R}+F_{w_L}).
\end{align}

By substituting the \eqref{eq:mod-polar-kin-coeff} in \eqref{eq:mod-dyn-equilibria}, the equilibrium equations are expressed in terms of accelerations of the center of mass in the robot frame:

\begin{align}
\dot{v}_u(t) &= v_w(t) \dot{\theta}(t) + \frac{F_{u_L}+F_{u_R}}{M} \label{eq:mod-dyn-equilibria2a} \\
\dot{v}_w(t) &= -v_u(t) \dot{\theta}(t)+\frac{F_{w_L}+F_{w_R}}{M}  \label{eq:mod-dyn-equilibria2b} \\
\ddot{\theta}(t) &= \frac{L}{J}(F_{u_R}-F_{u_L}) - \frac{c}{J}(F_{w_R}+F_{w_L}). \label{eq:mod-dyn-equilibria2c}
\end{align}

This is a general dynamic model (in the sense of no kinematic constraints) of a differential drive robot under the geometric assumptions listed above. It is noted that it is a coupled and nonlinear model, not exactly a best case scenario (we like linear things, because there are plenty of tools to handle them). When using the general dynamic model above, it makes sense to associate the general kinematic model as well, given by:

\begin{align} \label{eq:mod-gen-kin-mod}
\dot{x}_A(t) &= v_u(t) \cos\theta(t) - (v_w(t)-c \dot \theta)\sin\theta(t) \\
\dot{y}_A(t) &= v_u(t) \sin\theta(t) + (v_w(t)-c \dot \theta)\sin\theta(t).
\end{align}

the above \eqref{eq:mod-gen-kin-mod} can be obtained by recalling on one side that translations are isometric transformations, and on the other side that:

\begin{align} \label{eq:mod-xCW}
\left\{  \begin{array}{ll} x_A(t) &= x^W_C(t) - c \cos\theta(t) \\
                           y_A(t) &= y^W_C(t) - c \sin\theta(t) \end{array} \right.
\end{align}

\begin{align} \label{eq:mod-xCI}
\left\{  \begin{array}{ll} x_C^I(t) &=  v_u(t) \cos\theta(t) - v_w(t) \sin\theta(t) \\
                           y_C^I(t) &= v_u(t) \sin\theta(t) + v_w(t) \cos\theta(t) \end{array} \right.
\end{align}

Note: Equation \eqref{eq:mod-gen-kin-mod} can be rewritten as: \[ \label{eq:mod-gen-kin-mod-better} \avec{v_A^I} = \amat{R}(\theta) \avec{v_A^R} \], where: \[ \label{eq:mod-v_A^R} \avec{v_A^R} = [v_u(t), v_w(t) - c\dot\theta(t)]^T. \]

In order to simplify the model, we proceed to impose some kinematic constraints.

## Kinematics {#mod-kinematics}

In this section we derive the kinematic model of a differential drive mobile platform under the assumptions of (a) no lateral slipping and (b) pure rolling of the wheels. We refer to these two assumptions as kinematic constraints.

### Differential drive robot kinematic constraints {#mod-kin-constraint}
The kinematic constraints are derived from two assumptions:

- _No lateral slipping motion_: the robot cannot move sideways, but only in the direction of motion, i.e., its lateral velocity in the robot frame is zero:
\[ \label{eq:mod-no-lat-slip-constraint-r}
 \dot y_A^r = 0.
\]

 By inverting \eqref{mod-rotation-r2i}, this constraint can be expressed through the inertial frame variables, yielding:

\[ \label{eq:mod-no-lat-slip-constraint-i}
\dot y_A(t) \cos \theta(t) -\dot x_A(t) \sin \theta(t) = 0.
\]

Imposing \eqref{eq:mod-no-lat-slip-constraint-i} on \eqref{eq:mod-A-dot-polar} results in:

\[ \label{eq:mod-no-lat-slip-constraint-v_w}
v_w(t) = \dot y_C^I(t) \cos\theta(t) - \dot x_C^I(t) \sin\theta(t),
\]

and by recalling that $C^R = (c,0)$:

\[ \label{eq:mod-no-lat-slip-constraint-C}
\dot y_C^I(t) \cos\theta(t) - \dot x_C^I(t) \sin\theta(t) = c\dot\theta(t).
\]

Hence, we obtain the strongest expression of this constraint:

\[ \label{eq:mod-no-lat-slip-final}
v_w(t) = c\dot\theta(t),
\]

and therefore:

\[ \label{eq:mod-no-lat-slip-final-dot}
\dot v_w(t) = c\ddot\theta(t).
\]

Note: a simpler way of deriving \eqref{eq:mod-no-lat-slip-final-dot} is noticing, from \eqref{eq:mod-v_A^R}, that $\dot y_A^R = v_w(t) - c\dot\theta(t)$. 

- _Pure rolling_: the wheels never slips or skids ([](#fig:mod-pure-rolling)). Recalling that $R$ is the radius of the wheels (identical) and letting $\dot \varphi_{l}, \dot \varphi_{r}$ be the angular velocities of the left and right wheels respectively, the velocity of the ground contact point P in the robot frame is given by:

<div figure-id="fig:mod-pure-rolling" figure-caption="Pure rolling kinematic constraint">
  <img src="mod-pure-rolling-simpler.png" style='width: 15em; height:auto'/>
</div>

\begin{align} \label{eq:mod-pure-rolling}
\left\{  \begin{array}{ll} v_{P,r} &= R \dot \varphi_{r} \\
                      v_{P,l} &= R \dot \varphi_{l}  \end{array} \right..
\end{align}

Another notable consequence of this assumption is that, always in the robot frame, the full power of the motor can be translated into a propelling force for the vehicle in the longitudinal direction. Or, more simply, it allows to write:

\[ \label{eq:mod-force-and-torque}
F_{u, (\cdot)}(t)R = \tau_{(\cdot)}(t),
\]

where $\tau_{(\cdot)}(t)$ is the torque exerted by each motor on its wheel $(\cdot) = {l,r}$.

<!--
Recalling that the robot is assumed to be a rigid body, the velocity of point $P$ in the inertial frame can be expressed as the sum of the translational velocity $\avec{v_A}$ and that of the rotating field $\avec{w_P^I} = L \dot \theta$ due to the robot's rotation. The $X_I,Y_I $ components of $\avec{v_P}$ can therefore be expressed as:

\begin{align} \label{eq:mod-pure-rolling-inertial-left}
\left\{  \begin{array}{ll} \dot x_{P,r} &= \dot x_A + L\dot \theta \cos \theta \\
                      \dot y_{P,r} &= \dot y_A + L \dot \theta \sin \theta  \end{array} \right. ,
\end{align}

and

\begin{align} \label{eq:mod-pure-rolling-inertial-right}
\left\{  \begin{array}{ll} \dot x_{P,l} &= \dot x_A + L\dot \theta \cos \theta \\
                      \dot y_{P,l} &= \dot y_A + L \dot \theta \sin \theta  \end{array} \right..
\end{align}

By recalling \eqref{eq:mod-orthogonality-cond} and \eqref{eq:mod-no-lat-slip-constraint-r}, the expression of left and right wheel velocities in the robot frame can be summarized in the _pure rolling constraint_ equation:

\begin{align} \label{eq:mod-pure-rolling-constraint}
\left\{  \begin{array}{ll} \dot x_{P,r} \cos \theta +  \dot y_{P,r} \sin \theta &= R \dot \varphi_r \\
                           \dot x_{P,l} \cos \theta +  \dot y_{P,l} \sin \theta &= R \dot \varphi_l                 \end{array} \right..
\end{align}
-->
<!-- The following is useful in the Laplacian approach
### Kinematic constraints summary

Note: The kinematic constraints (\eqref{eq:mod-no-lat-slip-constraint-i}, \eqref{eq:mod-pure-rolling-constraint}) of a differential drive robot can be succinctly expressed as: \[ \label{eq:mod-constraints-succint} \amat{\Lambda}(\avec{q})\avec{\dot q} = 0,\]

where:

\begin{align} \label{eq:mod-lambda}
 \amat{\Lambda}(\avec{q}) = \left[ \begin{array}{ccccc} -\sin \theta & \cos \theta & 0 & 0 & 0 \\
                                                 \cos \theta & \sin \theta & L & -R & 0 \\
                                                 \cos \theta & \sin \theta & -L & 0 & R \\
   \end{array}  \right]
\end{align}

and:

\[ \label{eq:mod-q} \avec{\dot q} = \left[ \dot x_A \quad \dot y_A \quad \dot \theta \quad \dot \varphi_r \quad \dot \varphi_l \right]^T,  \]

\begin{align} \label{eq:mod-pure-rolling-relabel}
\left\{  \begin{array}{ll} v_{r} &= R \dot \varphi_{r}\\
                      v_{l} &= R \dot \varphi_{l}  \end{array} \right..
\end{align}
-->
## Differential drive robot kinematic model {#mod-kin}

In a differential drive robot, controlling the wheels at different speeds generates a rolling motion of rate $\omega = \dot \theta$.  In a rotating field there always is a fixed point, the _center of instantaneous curvature_ (ICC), and all points at distance $d$ from it will have a velocity given by $\omega d$, and direction orthogonal to that of the line connecting the ICC and the wheels (i.e., the _axle_). Therefore, by looking at [](#fig:mod-kin), we can write:

<!--

<div figure-id="fig:mod-kin-icc" figure-caption="By controlling the rotation rates of the wheel independently, a differential drive robot can make turns. Figure adapted from [](#bib:Dudek10).">
  <img src="mod-kin-icc.png" style='width: 30em; height:auto'/>
</div>

TODO: change labels in pic to match previously used conventions. $R$ in figure is $d$ in this text, and L in text is l/2 in pic.

-->

\begin{align} \label{eq:mod-kin-1}
\left\{  \begin{array}{l} \dot \theta (d-L) &= v_l  \\
                          \dot \theta (d+L)  &= v_r \end{array} \right.,
\end{align}

from which:

\begin{align} \label{eq:mod-kin-2}
\left\{  \begin{array}{l} d &= L \frac{v_r + v_l}{v_r - v_l}  \\
                          \dot \theta &= \frac{v_r - v_l}{2L} \end{array} \right..
\end{align}

A few observations stem from \eqref{eq:mod-kin-2}:

- If $v_r = v_l$ the bot does not turn ($\dot \theta = 0$), hence the ICC is not defined;
- If $v_r = - v_l$, then the robot "turns on itself", i.e., $d=0$ and $ICC \equiv A$;
- If $v_r = 0$ (or $v_l = 0$), the rotation happens around the right (left) wheel and $d = 2L$ ($d = L$).

Note: Moreover, a differential drive robot cannot move in the direction of the ICC, it is a singularity.

By recalling the _no lateral slipping motion_ \eqref{eq:mod-no-lat-slip-constraint-r} hypothesis and the _pure rolling_ constraint \eqref{eq:mod-pure-rolling}, and noticing that the translational velocity of $A$ in the robot frame is $v_A = \dot \theta d = (v_r+v_l)/2$ we can write:

\begin{align} \label{eq:mod-kin-3}
\left\{  \begin{array}{l} \dot x_A^R &= R (\dot \varphi_R +\dot \varphi_L)/2  \\
                          \dot y_A^R &= 0 \\
                          \dot \theta &= \omega = R(\dot \varphi_R - \dot \varphi_L)/(2L) \end{array} \right.,
\end{align}  

which in more compact yields the _simplified forward kinematics_ in the robot frame:

\begin{align} \label{eq:mod-forward-kinematics-robot-frame}
  \left[ \begin{array}{c} \dot x_A^R \\ \dot y_A^R \\ \dot \theta \end{array} \right] = \left[ \begin{array}{cc} \frac{R}{2}  & \frac{R}{2}  \\
                            0 & 0   \\
                            \frac{R}{2L} & -\frac{R}{2L}   \\  \end{array}  \right]  
                             \left[ \begin{array}{c} \dot \varphi_R \\ \dot \varphi_L \end{array} \right].
\end{align}

Finally, by using \eqref{eq:mod-rot-mat}, we can recast \eqref{eq:mod-forward-kinematics-robot-frame} in the inertial frame.

Note: The _simplified forward kinematics_ model of a differential drive vehicle is given by:
\begin{align} \label{eq:mod-forward-kinematics-inertial-frame}
\displaystyle \avec{\dot q}^I = \amat{R}(\theta)  \left[ \begin{array}{c} \dot x_A^r \\ \dot y_A^r \\ \dot \theta \end{array} \right] = \left[ \begin{array}{cc} \frac{R}{2} \cos \theta & \frac{R}{2} \cos \theta \\
\frac{R}{2} \sin \theta & \frac{R}{2} \sin \theta   \\
  \frac{R}{2L} & -\frac{R}{2L}   \\  \end{array}  \right]  
 \left[ \begin{array}{c} \dot \varphi_R \\ \dot \varphi_L \end{array} \right] = \left[ \begin{array}{cc} \cos \theta & 0 \\
                             \sin \theta & 0   \\
                             0 & 1   \\  \end{array}  \right]  
                              \left[ \begin{array}{c} v_A \\ \omega \end{array} \right].
\end{align}

## Simplified dynamic model {#mod-dyn-simpler}

By implementing the kinematic constraints formulations derived above, i.e., the no lateral slipping (\eqref{eq:mod-no-lat-slip-final-dot}) and pure rolling (\eqref{eq:mod-force-and-torque}) in the general dynamic model, it is straightforward to obtain:

\begin{align} \label{eq:mod-dyn-model-a}
\dot{v}_u (t) &= c \dot \theta^2(t) + \frac{1}{RM} (\tau_R(t)+\tau_L(t)) \\
\dot v_w(t) &= c \dot\theta(t) \\
\ddot \theta &= - \frac{Mc}{Mc^2+J} \dot\theta(t)v_u(t) + \frac{L}{R(Mc^2+J)}(\tau_R(t)-\tau_L(t))
\end{align}

<!--
Although \eqref{eq:mod-dyn-model-a} describes the dynamics of the robot, the input forces are difficult to measure. As it will be clearer from the next section where a model of the DC motor will be provided, it is more practical to consider the torques $(\tau_R, \tau_L) = (RF_{u_R}, RF_{u_L})$ in \eqref{eq:mod-dyn-model-a} as inputs to this system. By implementing this consideration and rearranging in matrix form:

\begin{align} \label{eq:mod-dyn-matrix-form}
\left[ \begin{array}{cc} M  & 0 \\
                          0 & Mc^2+J   \end{array}  \right] \left[ \begin{array}{c} \dot v_u \\ \ddot \theta \end{array} \right]+  
\left[ \begin{array}{cc} 0  & -Mc\dot\theta \\
                         Mc\dot\theta & 0  \end{array}  \right] \left[ \begin{array}{c}  v_u \\ \dot \theta \end{array} \right] = \frac{1}{R}\left[ \begin{array}{cc} 1  & 1 \\
                         L  & -L  \end{array}  \right] \left[ \begin{array}{c} \tau_R \\ \tau_L \end{array} \right].
\end{align}

This model now describes the input output relationship between torques and robot angular rate and velocities in the vehicle frame.

But there is still a missing link, as the actual control input to the robot is not the torque, but the voltage applied to the DC motors. It is hence necessary to model the actuator dynamics.
<!--
For example, given in the input torques $(\tau_R, \tau_L)$, this model yields $v_u(t), v_w(t)$ = c \dot \theta$, and $\theta(t)$, which through the inverse relation of \eqref{eq:mod-dyn-vC-to-vA} yields the velocity of $A$ in the inertial frame. In turn,-->
<!--

## Differential drive robot dynamic model {#mod-dyn}
While kinematics studies the properties of motions of geometric (i.e., massless) points, dynamical modeling takes into account the actual material distribution of the system. Once mass comes into play, motion is the result of the equilibrium of forces and torques. While different approaches can be used to derive these equations, namely the Lagrangian or Newtonian approaches (former based on energy considerations, latter on equilibrium of generalized forces), we choose to follow the Newtonian one here for it grants, arguably, a more explicit physical intuition of the problem. Obviously both methods lead to the same results when the same hypothesis are made.

### Notations {#mod-dyn-notations}

For starters, recalling that $C^r = (c, 0)$ is the center of mass of the robot, we define the relevant notations:

<div markdown="1">

 <col2 id='mod-dyn-notations' figure-id="tab:mod-dyn-notations" figure-caption="Notations for dynamic modeling of a differential drive robot">
    <s>$(v_u, v_w)$</s>  <s>Longitudinal and lateral velocities of $C$, robot frame</s>
    <s>$(a_u, a_w)$</s>  <s>Longitudinal and lateral accelerations of $C$, robot frame</s>
    <s>$(F_{u_R}, F_{u_L})$</s>  <s>Longitudinal forces exerted on the vehicle by the right and left wheels</s>
    <s>$(F_{w_R}, F_{w_L})$</s>  <s>Lateral forces exerted on the vehicle by the right and left wheels</s>
      <s>$(\tau_R, \tau_L)$</s>  <s>Torques acting on right and left wheel</s>
    <s>$\theta$, $\omega = \dot \theta$</s>  <s>Vehicle orientation and angular velocity</s>
    <s>$M$</s>  <s>Vehicle mass</s>
    <s>$J$</s>  <s>Vehicle yaw moment of inertia with respect to the center of mass $C$</s>
 </col2>

</div>
-->
<!--
### Free body diagram {#mod-dyn-fbd}

The next step, and definitely the most critical, is writing the free body diagram of the problem ([](#fig:mod-dyn)). In this analysis the only forces acting on the robot are those applied to the wheels.

Before proceeding with the equilibrium of forces and moments, it is appropriate to recall the expressions of velocities and accelerations of a rigid body in a rotating frame expressed in polar coordinates.

<div figure-id="fig:mod-dyn" figure-caption="Free body diagram of a differential drive robot">
  <img src="mod-fbd.png" style='width: 30em; height:auto'/>
</div>
-->
<!--
### Rotating frames in polar coordinates: a recap {#mod-dyn-rotating-polar}
### Equilibrium of forces and moments {#mod-dyn-eq status=draft}

We derive the dynamic model by imposing the simultaneous equilibrium of forces along the longitudinal and lateral directions in the robot frame with the respective inertial forces, and of the moments around the vertical axis (coming out of the.. screen) passing through the center of mass of the robotic vehicle.

\begin{align} \label{eq:mod-dyn-equilibria}
Ma_u(t) &= F_{u_L}+F_{u_R} \\
Ma_w(t) &= F_{w_L}-F_{w_R} \\
\ddot{\theta}(t) &= \frac{L}{J}(F_{u_R}-F_{u_L}) + \frac{c}{J}(F_{w_R}-F_{w_L})
\end{align}

By substituting the \eqref{eq:mod-dyn-polar-v-dv} in \eqref{eq:mod-dyn-equilibria}, the equilibrium of forces equations are expressed in terms of accelerations of the center of mass in the robot frame:

\begin{align}
\dot{v}_u(t) &= v_w \dot{\theta}(t) + \frac{F_{u_L}+F_{u_R}}{M} \label{eq:mod-dyn-equilibria2a} \\
\dot{v}_w(t) &= -v_u \dot{\theta}(t)+\frac{F_{w_L}-F_{w_R}}{M} \label{eq:mod-dyn-equilibria2b} \\
\ddot{\theta}(t) &= \frac{L}{J}(F_{u_R}-F_{u_L}) + \frac{c}{J}(F_{w_R}-F_{w_L}). \label{eq:mod-dyn-equilibria2c}
\end{align}

This general equation does not yet account for the the kinematic constraints discuss earlier.

Let the center of mass of the robot be identified by the vector $\avec{r}(t)$, as shown in [](#fig:mod-dyn)). The polar coordinated allow us to express $\avec{r}(t)$ using the complex notation:

\[ \label{eq:mod-dyn-r}
\avec{r}(t) = r(t) e^{j\theta(t)}.
\]

By differentiating in time \eqref{eq:mod-dyn-r}, and recalling the chain rule of derivatives, it is straightforward, although arguably boring to obtain the expression of radial velocity and acceleration, respectively:

\begin{align} \label{eq:mod-dyn-rd-rdd}
\avec{\dot r}(t) &= \dot{r}(t) e^{j\theta(t)} + j r(t) \dot \theta(t) e^{j\theta(t)} \\
\avec{\ddot r}(t) &= \ddot{r}(t) e^{j\theta(t)} + 2 j \dot{r}(t) \dot \theta(t) e^{j\theta(t)} + j r(t) \ddot{\theta}(t) e^{j\theta(t)} - r(t) \dot \theta^2 e^{j\theta(t)}.
\end{align}

By simplifying and writing the lateral components explicitly, \eqref{eq:mod-dyn-rd-rdd} becomes:

\begin{align} \label{eq:mod-dyn-rd-rdd2}
\avec{\dot r}(t) &= v_u(t) e^{j\theta(t)} +  v_w (t) e^{j\left(\theta (t)+\frac{\pi}{2}\right)} \\
\avec{\ddot r}(t) &= a_u(t) e^{j\theta(t)} +  a_w (t) e^{j\left(\theta (t)+\frac{\pi}{2}\right)},
\end{align}
### Equilibrium of forces and moments {#mod-dyn-eq status=draft}

We derive the dynamic model by imposing the simultaneous equilibrium of forces along the longitudinal and lateral directions in the robot frame with the respective inertial forces, and of the moments around the vertical axis (coming out of the.. screen) passing through the center of mass of the robotic vehicle.

\begin{align} \label{eq:mod-dyn-equilibria}
Ma_u(t) &= F_{u_L}+F_{u_R} \\
Ma_w(t) &= F_{w_L}-F_{w_R} \\
\ddot{\theta}(t) &= \frac{L}{J}(F_{u_R}-F_{u_L}) + \frac{c}{J}(F_{w_R}-F_{w_L})
\end{align}

By substituting the \eqref{eq:mod-dyn-polar-v-dv} in \eqref{eq:mod-dyn-equilibria}, the equilibrium of forces equations are expressed in terms of accelerations of the center of mass in the robot frame:

\begin{align}
\dot{v}_u(t) &= v_w \dot{\theta}(t) + \frac{F_{u_L}+F_{u_R}}{M} \label{eq:mod-dyn-equilibria2a} \\
\dot{v}_w(t) &= -v_u \dot{\theta}(t)+\frac{F_{w_L}-F_{w_R}}{M} \label{eq:mod-dyn-equilibria2b} \\
\ddot{\theta}(t) &= \frac{L}{J}(F_{u_R}-F_{u_L}) + \frac{c}{J}(F_{w_R}-F_{w_L}). \label{eq:mod-dyn-equilibria2c}
\end{align}

This general equation does not yet account for the the kinematic constraints discuss earlier.

where:

\begin{align} \label{eq:mod-dyn-polar-v-dv}
v_u(t) &= \dot{r}(t) \\
v_w(t) &= r(t) \dot \theta(t) \\
a_u(t) &= \ddot{r}(t) - r(t) \dot \theta^2 \\
a_w(t) &= 2 \dot{r}(t) \dot \theta(t) + r(t) \ddot \theta.
\end{align}

Exercise: prove that $je^{j\theta}=e^{j(\theta+\pi/2)}$.
-->
<!--
### Equilibrium of forces and moments {#mod-dyn-eq status=draft}

We derive the dynamic model by imposing the simultaneous equilibrium of forces along the longitudinal and lateral directions in the robot frame with the respective inertial forces, and of the moments around the vertical axis (coming out of the.. screen) passing through the center of mass of the robotic vehicle.

\begin{align} \label{eq:mod-dyn-equilibria}
Ma_u(t) &= F_{u_L}+F_{u_R} \\
Ma_w(t) &= F_{w_L}-F_{w_R} \\
\ddot{\theta}(t) &= \frac{L}{J}(F_{u_R}-F_{u_L}) + \frac{c}{J}(F_{w_R}-F_{w_L})
\end{align}

By substituting the \eqref{eq:mod-dyn-polar-v-dv} in \eqref{eq:mod-dyn-equilibria}, the equilibrium of forces equations are expressed in terms of accelerations of the center of mass in the robot frame:

\begin{align}
\dot{v}_u(t) &= v_w \dot{\theta}(t) + \frac{F_{u_L}+F_{u_R}}{M} \label{eq:mod-dyn-equilibria2a} \\
\dot{v}_w(t) &= -v_u \dot{\theta}(t)+\frac{F_{w_L}-F_{w_R}}{M} \label{eq:mod-dyn-equilibria2b} \\
\ddot{\theta}(t) &= \frac{L}{J}(F_{u_R}-F_{u_L}) + \frac{c}{J}(F_{w_R}-F_{w_L}). \label{eq:mod-dyn-equilibria2c}
\end{align}

This general equation does not yet account for the the kinematic constraints discuss earlier.
-->
<!--
### Imposing the kinematic constraints {#mod-dyn-eq-constrained}

Equations \eqref{eq:mod-dyn-equilibria} of motion can be decoupled by imposing the kinematic constraints \eqref{eq:mod-no-lat-slip-constraint-r} and \eqref{eq:mod-pure-rolling}. In particular, to impose the no lateral slipping hypothesis \eqref{eq:mod-no-lat-slip-constraint-r}, we first need to express the velocity of the center of mass of the robot in the inertial frame, then derive the velocity of point $A$ as a function of that in $C$, and finally impose the lateral velocity to be zero. To do so, we first need to notice that, in the inertial frame:
-->
<!--
Equations \eqref{eq:mod-dyn-equilibria} of motion can be decoupled by imposing the kinematic constraints \eqref{eq:mod-no-lat-slip-constraint-r} and \eqref{eq:mod-pure-rolling}. In particular, to impose the no lateral slipping hypothesis \eqref{eq:mod-no-lat-slip-constraint-r}, we need to express the velocity of $A$ in the local frame and set it to zero.

\begin{align} \label{eq:mod-dyn-vC-to-vA}
x_C &= x_A + c \\cos\theta \\
y_C &= y_A + c \\sin\theta
\end{align}


<!-- \label{eq:mod-dyn-vC-to-vA}-->
<!--
then recall that through the rotation matrix $\amat{R}(t)$:

\begin{align} \label{eq:mod-dyn-constraints-rot-refresh}
  \left[ \begin{array}{c} \dot x_C \\ \dot y_C \end{array} \right] = \left[ \begin{array}{cc} \\cos\theta  & -\\sin\theta  \\
  \\sin\theta  & \\cos\theta     \end{array}  \right]  
   \left[ \begin{array}{c} v_u \\ v_w \end{array} \right].
\end{align}

With these two conditions, it can be shown that $\dot y_A^r = v_w - c \dot \theta$. Hence, by imposing $\dot y_A^r = 0 \Rightarrow v_w = c \dot \theta$.
-->
<!--
By using this condition in \eqref{eq:mod-dyn-equilibria2a} and \eqref{eq:mod-dyn-equilibria2b}, and combining with \eqref{eq:mod-dyn-equilibria2c}, we obtain the dynamical equations of a differential drive robot under the aforementioned constraints:



\begin{align} \label{eq:mod-dyn-model-a}
 \dot{v}_u (t) &= c \dot \theta^2 + \frac{1}{M} (F_{u_L}+F_{u_R}) \\
         \ddot \theta &= \frac{L}{Mc^2+J}(F_{u_R}-F_{u_L}) + \frac{Mcv_u}{Mc^2+J} \dot \theta.
\end{align}

Although \eqref{eq:mod-dyn-model-a} describes the dynamics of the robot, the input forces are difficult to measure. As it will be clearer from the next section where a model of the DC motor will be provided, it is more practical to consider the torques $(\tau_R, \tau_L) = (RF_{u_R}, RF_{u_L})$ in \eqref{eq:mod-dyn-model-a} as inputs to this system. By implementing this consideration and rearranging in matrix form:

\begin{align} \label{eq:mod-dyn-matrix-form}
\left[ \begin{array}{cc} M  & 0 \\
                          0 & Mc^2+J   \end{array}  \right] \left[ \begin{array}{c} \dot v_u \\ \ddot \theta \end{array} \right]+  
\left[ \begin{array}{cc} 0  & -Mc\dot\theta \\
                         Mc\dot\theta & 0  \end{array}  \right] \left[ \begin{array}{c}  v_u \\ \dot \theta \end{array} \right] = \frac{1}{R}\left[ \begin{array}{cc} 1  & 1 \\
                         L  & -L  \end{array}  \right] \left[ \begin{array}{c} \tau_R \\ \tau_L \end{array} \right].
\end{align}
<!--
This model now describes the input output relationship between torques and robot orientation and forward speed. Although t -->
<!--
This model now describes the input output relationship between torques and robot orientation and forward velocity in polar coordinates and can be further manipulated to obtain relations between the input torques and relevant variables such as the angular rates of the wheels.

But there is still a missing link, as the actual control input to the robot is not the torque, but the voltage applied to the DC motors. It is hence necessary to model the actuator dynamics.
 -->
<!--
For example, given in the input torques $(\tau_R, \tau_L)$, this model yields $v_u(t), v_w(t)$ = c \dot \theta$, and $\theta(t)$, which through the inverse relation of \eqref{eq:mod-dyn-vC-to-vA} yields the velocity of $A$ in the inertial frame. In turn,-->


## DC motor dynamic model {#mod-motor}

The equations governing the behavior of a DC motor are driven by an input _armature voltage_ $V(t)$:

\begin{align}
V(t) &= Ri(t) + L \frac{di}{dt} + e(t) \\
e(t) &= K_b \dot\varphi(t)  \\
\tau_m(t) &= K_t i(t)  \\
\tau(t) &= N \tau_m(t),
\end{align}

where $(K_b, K_t)$ are the back emf and torque constants respectively and $N$ is the gear ratio ($N=1$ in the Duckiebot).

[](#fig:mod-dc-motor) shows a diagram of a typical DC motor.

<div figure-id="fig:mod-dc-motor" figure-caption="Diagram of a DC motor">
  <img src="mod-dyn-dc-motor-electrical.png" style='width: 30em; height:auto'/>
</div>

Having a relation between the applied voltage and torque, in addition to the dynamic and kinematic models of a differential drive robot, allows us to determine all possible state variables of interest.

Note: torque disturbances acting on the wheels, such as the effects of friction, can be modeled as additive terms (of sign opposite to $\tau$) in the DC motor equations.

<!--
[](#fig:mod-dynamic)

<div figure-id="fig:mod-dynamic" figure-caption="Free body diagram of a differential drive robot">
  <img src="mod-dynamic.png" style='width: 30em; height:auto'/>
</div>

## Final result {#mod-result status=draft}
-->
<!--
[](#fig:mod-final)

<div figure-id="fig:mod-final" figure-caption="Block diagram representation of the model of a differential drive robot">
  <img src="mod-final.png" style='width: 30em; height:auto'/>
</div>-->

## Conclusions {#mod-conclusions}

In this chapter we derived a model for a differential drive robot. Although several simplifying assumption were made, e.g., rigid body motion, symmetry, pure rolling and no lateral slipping - still the model is nonlinear.

Regardless, we now have a sequence of descriptive tools that receive as input the voltage signal sent by the controller, and produce as output any of the state variables, e.g., the position, velocity and orientation of the robot with respect to a fixed inertial frame.

Several outstanding questions remain. For example, we need to determine what is the best representation for our robotic platform - polar coordinates, Cartesian with respect to an arbitrary reference point? Or maybe there is a better choice?

Finally, the above model assumes the knowledge of a number of constants that are characteristic of the robot's geometry, materials, and the DC motors. Without the knowledge of those constant the model could be completely off. Determination of these parameters in a measurement driven way, i.e., the "system identification" of the robot's plant, is subject of the _odometry_ class.  

<!--
- assumptions: rigid body, same distance L, c from left/right wheel, friction and weight?, mass an inertias of wheels are not taken in consideration
-->














<!--

## Kinematics {#mod-kinematics status=draft}

A Duckiebot has two DC motors that independently control the front wheels.

The content of this chapter is taken from [](#bib:Dudek10).

<div class='requirements' markdown="1">

Requires: [k:intro-kinematics](#intro-kinematics),

Requires:[k:coordinate-systems](#coordinate_systems)

Result: k:car-kinematics

</div>

### Differential drive kinematics {#car-kinematics-diff-drive status=draft}

### Forward kinematics for differential drive robots {#car-kinematics-forward-kin status=draft}

### Inverse kinematics for differential drive robots {#car-kinematics-inverse-kin status=draft}

### Duckiebot kinematics {#car-kinematics-duckiebot status=draft}

-->
