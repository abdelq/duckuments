# System architectures basics {#system-architectures-basics status=draft}

Assigned: Andrea Censi

<div class='requirements' markdown="1">

Results: Physical and logical architectures.

Results: Deployment as mapping a physical architecture onto the logical.

Requires: Basic graph concepts.

Requires: Basic operating systems concepts.

</div>




## Logical and physical architecture {#logical-vs-physical}

When we design a robotic system, or any cyber-physical system, we distinguish
between what we shall call "logical architecture" and the "physical
architecture".

The logical architecture describes how the functionality is divided in abstract
modules, and what these modules communicate.

The physical architecture describes how the modules are instantiated. For
example, this includes the information of how many processors  are used, and
which processor runs which routine.


## Logical architecture {#logical-architectures}

The logical architecture is independent of the implementation (the
hardware, the language.)

The logical architecture describes:

- The system decomposition in components
- The data flow: who tells whom what
- How knows what: other sources of information, such as priors.
- How information is represented

A logical architecture would also describe what are the representations used.
This is explored more fully in [the unit about representations](#representations).

## Actor model

TODO: Brief discussion of actor model


## Physical architecture {#physical-architectures}

TODO: Processors

TODO: Buses / networks

TODO: Middleware

TODO: Orchestrators

TODO: In ROS that is the `roscore` program.

## Mapping logical architecture onto physical

For deployment, one must choose how the logical architecture is mapped on the
physical architecture.

This can be seen as a graph mapping problem.

One can define a computation graph as a graph where nodes are algorithms and
edges are events.

A resource graph is a graph where nodes are processors and edges are
communication channels.

Given a computation graph and a resource graph one must choose where to put
each node in the computation graph in the resource graph.

Remark: More formally, the assignment is called a graph homomorphism.

## Example in Duckietown

You will see a concrete example of different ways to map software components
on logical architectures in one of the first exercises.

Duckietown uses ROS. In ROS, the components are called *nodes*.
In ROS, the granularity is at the level of hosts rather than processors.
In regular vanilla Linux, the kernel decides which physical processor
executes which process at any time.

In ROS, the assignment of nodes to processors happens using
a *launch file*.

By modifying the launch file we can choose the layout of the computation.

Typically you will encounter three ways to deploy a graph:

1. **Running everything on the robot.** This is the regular "autonomous" mode.

2. **Running everything on the robot, but orchestrating from the laptop**. In this
case, the `roscore` program runs on a laptop, and the other components on the robot.

3. **Running heavy computation on the laptop**. In this mode,
the heavy computation processes run on the laptop, while the actuation and sensing drivers run on the robot.


## Take-away points

* The logical architecture describes the system decomposition, independent of the implementation.

* The physical architecture describes how is the computation physically realized.

* There are multiple ways to map a _computation graph_ onto a _resource graph_. This is something that is immediately useful to understand for rapid development.


## Further reading


* E. A. Lee and S. A. Seshia, <a href="http://LeeSeshia.org">Embedded Systems -- A Cyber-Physical Systems Approach</a>, MIT Press, Second Edition, 2017.

<!-- * A paper about the optimization of computation graph deployments. XXX
* Some generic reference about real-time systems. XXX -->
