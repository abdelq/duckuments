# Learning in Duckietown {#learning-duckietown lang=en status=draft type=text}

Assigned: Jacopo

Note: This chapter is a draft.


> Bad: We do not refer to teachers and students

> Better: We refer to learners. Instructors are learners ahead in the learning curve in comparison to other learners

> Bad: We don't examinate

> Better: We assess competences


## The learning feedback loop {#learning-feedback}

A relevant contribution of modern educational theory is recognizing the importance of feedback in the learning process (). 

We love feedback, as it stands at the foundation of control systems theory. 

<div figure-id="fig:learning-feedback-loop" figure-caption="The learning loop.">
     <img src="learning-feedback-loop.png" style='width: 30em'/>
</div>

Here, we provide definitions of the key elements in a learning feedback loop, and analogies to their control systems counterparts.

### Intended Learning Outcomes {#ilo}

\begin{definition}[Intended Learning Outcome]   \label{def:ilo}
An intended learning outcome is a desired, _measurable_, output of the learning process. 
\end{definition}

Intended learning outcomes are:

- the starting point in the construction of a learning activity ([](#bib:tani16duckietown)),

- more effective when formulated with active verbs,

- the equivalent of reference trajectories, or setpoints, in control systems. They represent the ideal output of the controlled system.

<div class='example-usage' markdown="1">

> Bad: Students will understand robotics

> Better: Students each build a Duckiebot, implement software and produce demos

</div>

### Learning Activities {#learning-activities}

\begin{definition}[Learning Activities]   \label{def:learning-activity}
Methods chosen by the instructor to ease the learners achievement of the intended learning outcomes.
\end{definition}

_Active learning_ practices ([](#bib:tani16duckietown)) have been shown to improve learning.

<div class='example-usage' markdown="1">

> Bad: Instructor explains at the blackboard

> Better: Learners work in groups to achieve objectives

</div>

Learning activities are analogous to the the output of the controller (instructor), or input to the system (learners). They have to meet the requirements imposed by external constraints, not shown in 

### Assessment {#assessment}

\begin{definition}[Assessment]   \label{def:assessment}
An assessment is a procedure to quantify the level of fulfillment of learning outcomes.
\end{definition}

An assessment is analogous to a sensor in a control system loop. It measures the system's output.

<div class='example-usage' markdown="1">

Examples of assessments include: quizzes, colloquia, produced documentation, homework, etc.

</div>


## Knowledge, Skills and Competences {#ksc}

Here, we provide definitions for knowledge, skills and competences, in addition to describing their relationships ([](#fig:ksc)). 

<div figure-id="fig:ksc" figure-caption="The relationship between Knowledge, Skills and Competences.">
     <img src="ksc.png" style='width: 30em'/>
</div>


### Knowledge {#knowledge}

\begin{definition}[Knowledge]   \label{def:knowledge}
Theoretical facts and information aimed at enabling understanding, and generating or improving _skills_. 
\end{definition}

<div class='example-usage' markdown="1">

Bayesian inference is handy piece of knowledge when doing robotics.

</div>


### Practice {#practice}

\begin{definition}[Practice]    \label{def:practice}
Practical procedures aimed at generating or improving _skills_, either directly or indirectly by improving knowledge.
\end{definition}

<div class='example-usage' markdown="1">

Exercises and proofs can be used to practice different skills.

</div>

### Skills {#skills}

\begin{definition}[Skills]    \label{def:skills}
A proficiency, facility or dexterity that enables carrying out a function. Skills stem from _knowledge_, _practice_ and/or aptitude. Skills can be clustered in cognitive, technical and interpersonal, respectively relating to ideas, things and people. 
\end{definition}

<div class='example-usage' markdown="1">

Analyzing tradeoffs between performances and constraints is a critical cognitive skill for robotics.

Python language is a useful technical skill in robotics.

Public speaking is a valuable interpersonal skill useful beyond robotics.

</div>

In Duckietown we formalize didactic indivisible units, or [_atoms_](#knowledge-graph), aimed at improving skills through knowledge and practice. Knowledge atoms are listed in XXX. We define as practice atoms:

TODO: add general reference to all learning atmos, folder atoms_30_learning_material

\begin{definition}[Exercise]    \label{def:exercise}
An exercise is a practice atom aimed at improving technical skills. Exercises are listed in XXX.
\end{definition}

Exercises are targeted to different "things" to which technical skills are related. They may be mathematical exercises aimed at practicing a method, or they may be coding exercises aimed at practicing resolutions of hardware implementation challenges.

\begin{definition}[Proof]    \label{def:proof}
A proof is a practice atom aimed at improving cognitive skills.
\end{definition}

<div class='example-usage' markdown="1">

Deriving the Kalman filter equations helps practice the _idea_ that there is no better approach to state estimation for linear time invariant systems, with "well behaved" measurement and process noises. 

</div>

### Competences {#competences}

\begin{definition}[Competences]    \label{def:competences}
Set of skills and/or knowledge that leads to superior performance in carrying out a function. Competences must be _measurable_.
\end{definition}

Competences are desirable intended learning outcomes, and typically address the _how_ of the learning process.

<div class='example-usage' markdown="1">

Programming is a competence. It requires a skill, e.g., Python, and knowledge, e.g., Bayesian inference, to know what to code. Practice can help improve knowledge or hone skills.

</div>

<!-- ## From theory to the Duckiebook {#} --> 

<!-- How does the above relate, practically, to the Duckiebook? {k,s,c,p}-atoms? --> 

