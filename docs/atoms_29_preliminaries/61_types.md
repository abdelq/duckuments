# Types {#types status=beta}

<div class='requirements' markdown='1'>

Results: Introduction to type theory.

Requires: Knowledge of [set theory](#sets).

</div>

## Types vs sets

Types are similar to sets in that they are collections that include some objects and exclude others. On a first glance, you can interpret $0 : \text{nat}$ as $0 \in \mathbb{N}$, reading the colon as membership in sets without any ill effect. But types and sets are the basic concepts belonging to two different formal systems, _type theory_ and _set theory_, respectively. It is not essential to appreciate the difference in the scope of this course but for the curious readers, [this section on Wikipedia](https://en.wikipedia.org/wiki/Type_theory#Difference_from_set_theory) can serve as a brief summary.

## Example: product types

Given two types $A$ and $B$, we can construct the type $A \times B$, which we call their _cartesian product_. (Compare this with the similar concept of _cartesian product of sets_ which is defined in terms of its elements and not a primitive.)

## In Duckietown

As we will be using ROS, which models a robotic system as a network of communicating programs. In order to understand each other, all the communicating programs talk to each other in well-defined _message types_. Message types in ROS are product types composed of primitive types and other message types.

<div class='check' markdown="1">
Please read section 2 on [ROS/msg page](http://wiki.ros.org/msg) and answer: what are some primitive types in ROS? what are the fields and their types in message type `Header`?
</div>

Additionally, [ROS/common_msgs page](http://wiki.ros.org/common_msgs) provides a list of pre-defined message types commonly used in robotics, such as [Image](http://docs.ros.org/api/sensor_msgs/html/msg/Image.html) (note how `Header`, a non-primitive type, is included in the definition) and [Pose2D](http://docs.ros.org/api/geometry_msgs/html/msg/Pose2D.html). As you have likely guessed, an RGB camera publishes `Image` messages, and a routing planning program might subscribe to the duckiebot's current position in duckietown, as represented in a `Pose2D` message and calculates the appropriate wheel actions.

## Historical notes

Historically, the flexibility of naive set theory allows for some paradoxical sets such as a set that contains all sets that does not contain itself. Does this set contains itself? This is known as [Russell's paradox](https://en.wikipedia.org/wiki/Russell%27s_paradox) which demonstrated that naive set theory is inconsistent. In response, Russell and colleagues developed type theory which demands all terms to be _typed_, i.e., to have a type, and used a hierarchy of types to avoid Russell's paradox. Later, a subclass of type theories known as intuitionistic type theories internalized many key ideas in constructive mathematics and became a foundation for programming languages where _computability_ is a major concern.

On a side note, this is not to say sets cannot serve as a formal foundation of mathematics. Russell's paradox only shows that _naive_ set theory is _inconsistent_. In fact, most working mathematicians today believe that the axiomatized [Zermelo-Fraenkel set theory](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory) (together with the axiom of choice, usually abbreviated as ZFC) can serve as a "consistent" foundation of all mathematics.

## Further reading

Type theory is a fascinating subject in itself and recently, Homotopy Type Theory (HoTT) captured a lot of research interest. For more on the subject consult [HoTT website](https://homotopytypetheory.org/). The first chapter of the HoTT book also provides a reasonable introduction to type theory. For more practical applications of these abstract ideas, you may be intrigued by the field of [formal verification](https://en.wikipedia.org/wiki/Formal_verification), where software is verified by mathematical proofs against the formal specification, automatically.

Author: Falcon Dai

Maintainer: Falcon Dai
