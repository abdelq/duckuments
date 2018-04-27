# Chapter template {#theory-chapter-template status=ready}

Theory chapters benefit from a standardized exposition. Here, we define the template for these chapters. Rememeber to check [](#sec:documentation-manual) for a comprehensive and up-to-date list of Duckiebook supported features.

## Example Title: PID control {#pid-example-theory-label}

[//]: # (Start copying and pasting template from here)

Start with a brief introduction of the discussed topic, describing its place in the bigger picture, justifying the reading constraints/guidelines below. Write it as if the reader knew the relevant terminology. For example:

PID control is the simplest approach to making a system behave in a desired way rather than how it would naturally behave. It is simple because the measured output is directly feedbacked, as opposed to, e.g., the system's states. The control signal is obtained as a weighted sum of the tracking error (_P_roportional term), its integral over time (_I_ntegrative term) and its instantaneous derivative (_D_erivative term), from which the appellative of PID control. The tracking error is defined as the instantaneous difference between a reference and a measured system output.

<div class='requirements' markdown="1">

Knowledge necessary:

Required Reading: Insert here a list of topics and suggested resources related to _necessary_ knowledge in order to understand the content presented. Example:

Requires: Terminology: [autonomy overview](#autonomy-overview)

Requires: System Modeling: [basic kinematics](#intro-kinematics), [basic dynamics](#intro-dynamics), [linear algebra](#linear_algebra), [State space representations](), [Linear Time Invariant Systems]()

</div>

<div class="requirements" markdown="1">

Suggested Reading: Insert here a list of topics and suggested resources related to _recommended_ knowledge in order to better understand the content presented. Example:

Recommended: Definitions of Stability, Performances and Robustness: [](#bib:placeholder), ...

Recommended: observability/detectability and controllability/reachability: [](#bib:placeholder)

Recommended: Discrete time PID: [](#bib:placeholder)

Recommended: Bode diagrams: [](#bib:placeholder)

Recommended: Nyquist plots: [](#bib:placeholder)

Recommended: [...]

</div>


## Problem Definition {#theory-chapter-template-problem-def}

In this section we crisply define the problem object of this chapter. It serves as a very brief recap of exactly what is needed from previous atoms as well. E.g.

Let:

\begin{align}
\dot{\state}_t = A\state_t+Bu_t \\
y = C\state_t+Du_t              \label{eq:system}
\end{align}

 be the LTI model of the Duckiebot's plant, with $x \in \statesp$, $y \in \mathbb{R}^p$ and $u \in \mathbb{R}^m$. We recall ([Duckiebot Modeling]()) that:

\begin{align}
A &= \left[  \begin{array}{ccc} a_{11}  & \dots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{n1}  & \dots & a_{nn} \end{array} \right] \\
B &= \left[ b_1 \,\, \dots \,\, b_m \right]^T \\
C &=  \left[ c_1 \ \,\, \dots \,\, c_p \right] \\
D &= 0.
\end{align}

[...]

Remember you can use the `problem` environment of $\LaTeX$ to formally state a problem:

\begin{problem}[PID]\label{prob:label-prob}
Given a system \eqref{eq:system} and measurements of the output $\tilde{y}_t = y_t + n_t, n_t \sim \cal{N}(0,\sigma)$, find a set of PID coefficients that meet the specified requirements for:
- stability,
- performance,
- robustness.
\end{problem}

as shown in ([](#figure:the-bigger-picture)).

<div figure-id="fig:the-bigger-picture" figure-caption="A classical block diagram for PID control. We like to use a lot of clear figures in the Duckiebook.">
     <img src="placeholder.png" style='width: 15em'/>
</div>

## Introduced Notions {#theory-chapter-template-notions}

### Section 1: title-1 (e.g.: Definitions)

\begin{definition}[Reference signals]\label{def:def-label}
A reference signal $\tilde{y}_t \in \mathcal{L}_2(\mathcal{T})$ is ...
\end{definition}

[](#def-label) is very important.

<div class="check" markdown="1">

Insert 'random' checks to keep the reader's attention up:

if you can't be woken up in the middle of the night and remember the definition of $\mathcal{L}_2(\cdot)$, read: [](#bib:placeholder)

</div>

\begin{definition}[Another definition]\label{def:another-def-label}
Lorem
\end{definition}

### Section 2: title-2 (e.g.: Output feedback)

Now that we know what we're talking about, lets get in the meat of the problem. Here is what is happening:

\[ \cal{Lorem}
\]

### Section 3: title-3 (e.g.: Tuning the controller)

Introduce the 'synthesis through attempts' methodology (a.k.a. tweak until death)

### Section 4: title-4 (e.g.: Performance Metrics)

How do we know if the PID controller designed above is doing well? We need to define some performance metrics first:

Overshoot, Module at resonance, Settling Time, Rising Time

[...]

<div class="example-usage" markdown="1">

This is a 'think about it' interrupt, used as attention grabber:

When a Duckiebot 'overshoots', it means that [...] and the following will happen [...].

</div>

### Section N: title-N (e.g.: Saving the world with PID)

And finally, this is how you save the world, in theory.

## Examples {#theory-chapter-template-examples}

This section serves as a collection of theoretical and practical examples that can clarify part or all of the above.

### Theoretical Examples {#theory-chapter-template-examples-theory}

More academic examples

#### T-Example 1

Immagine a spring-mass-damper system...

#### T-Example M

[...]

### Implementation Examples {#theory-chapter-template-examples-code}

More Duckiebot related examples

#### I-Example 1


#### I-Example M

[...]

## Pointers to Exercises {#theory-chapter-template-exercises-pointers}

Here we just add references to the suggested exercises, defined in the appropriate [exercise chapters](#part:exercises).


## Conclusions

- What did we do? (recap)
- What did we find? (analysis)
- Why is it useful? (synthesis)
- Final Conclusions (what have we learned)

## Next Steps

Strong of this new knowledge (what have we learned), we can now [...].

<!--(Dear Santa, I would like class='additional-reading' here) -->
<div class="requirements" markdown="1">

Further Reading: insert here reference resources for the interested reader:

See also: learn all there is to know about PID: [](#bib:placeholder)

See also: become a linear algebra master: [Matrix cookbook](#bib:matrix-cookbook)

</div>

[//]: # (End copying and pasting template from here)

## References {#bibliography-example-theory-label}

Do not include a reference chapter. References are automatically compiled to [the Bibliography Section](#bibliography).


Author: Jacopo

Maintainer: Jacopo

Point of Contact: Jacopo
