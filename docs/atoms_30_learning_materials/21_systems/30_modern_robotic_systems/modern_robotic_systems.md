# Modern Robotic Systems {#modern-robotic-systems status=draft}

Assigned: Andrea Censi

<div class='requirements' markdown='1'>

Results: The many parts of a robotic system

Results: Modern robotics development

Results: Example of cloud learning, annotators in the loop scenario.

</div>

## No robot is an island

A robot is only a small part of a modern robotic system.

We briefly discuss what we could consider the possible components of a robotic
system.

Of course, **the robot**, which includes:

- The hardware: actuation, sensing, computation;
- The software;

**The other robots** with which the robot interacts. Perhaps they just need to avoid each other; perhaps they are collaborating.

The **other machines**. For example, a battery dock with that the
robot can use to recharge

The **infrastructure**, including the network and off-board
storage and computation resources.

The **people**, including:

  - The supervisors;
  - The safety operator;
  - The customers;
  - ...


## Development of modern robotic systems

While robotic systems have existed for decades, modern autonomous robotic
systems are developed in a different way than traditional robotics/automation
projects.

The classical model of development consists of:

* design;
* product development;
* integration (by "system integrators");
* installation;
* support.

These are instead the characteristics of modern robotics development model:

- continuous feedback from the users
- learning from data, acquired by the robot
- continuous integration
- incremental updates
- agile development

<!-- ### Industry 4.0

A buzzword they use in Europe -->


## Example of a typical data processing pipeline

<!-- We provide a description of a typical data processing pipeline
that is based on the cloud.  -->

Variations on the following idea are what is typically implemented
by autonomous vehicles developers for object detection.

The problem is to implement a machine-learning system that
learns to perform an object detection task based on supervised learning.

Training and validation happen on large datasets that are continuously
updated with new data coming from the cars, and new annotations coming
from annotators.

### The cloud as a component

We can consider "the cloud" as a component of a modern robotic
system. The cloud can be modeled as a component that provides:

- Essentially "infinite" computation;
- Essentially "infinite" storage;
- Very large latency.

Because of the latency, it is not possible for real-time robotics
applications to run completely on the cloud.

Therefore, the cloud is much more useful for tasks like the following:

- running simulations;
- training machine learning models;
- running regression tests.

As of 2017, the largest cloud-computing services are the ones offered by
Amazon (AWS), Microsoft (Azure), Google (Google Cloud).

### The annotators as components

For supervised learning tasks, one needs to have large annotations databases.

The idea of using human annotators as a "software service" was first deployed
on a large scale by Amazon with the "Mechanical Turk" project.

Nowadays, there exist companies that are specialized in providing
annotations for AI tasks.

Examples of annotation services are:

* [MightyAI][mightyAI]: "Training Data as a Service"
* [Samasource][samasource]

[mightyAI]: https://mty.ai/
[samasource]: https://www.samasource.org/

### Putting it all together in feedback

Now that we have introduced the components, we will see how
one can put everything together in a system ([](#fig:modern-data)).

<div figure-id="fig:modern-data">
    <figcaption>Example of modern data-based pipeline</figcaption>

    <img src='example_cloud_architecture.png' style='width: 80%; height: auto'/>
</div>


This system works as follows:

1. The robots collect data during normal operation.
2. The data becomes part of a large cloud-base storage.
2. The data is divided in training and validation data.
5. Continuously, a new model is trained based on the latest data.
6. The new candidate model is evaluated using regression tests; the goal
   is to outperform the previous model.
3. The new models are broadcast to the robots.
4. The regression tests also look for which new data is most useful to annotate,
   and this information is passed to the annotators, who create more annotations.
3. The regression tests also look for which new data would be interesting to collect,
   and this is done by a dedicated car.


## Vignettes from an optimistic future

In the near future, it might be that the design of robotic systems
might become even more complicated.
For example, it might be that blockchain technologies will allow
machines to trade between them.

<div class='example-usage' markdown='1'>
A self-driving car realizes it is too dirty; by itself, it finds a robotic
carwash, and together they agree on the time and the price, and the car pays by
itself using Bitcoin.
</div>

## Take-away points

- The robot is but a small part of a robotic system.

- Development methods have changed recently: data is very important,
  as well as delocalized computation.

## Further reading

* One of the cloud robotics papers XXX

* Mechanical Turk XXX

* The [Robot Design Game][rdg]

* A Blockchain tutorial XXX



[rdg]: http://robot-design.org

<!--
## Examples in Duckietown

* A cloud-in-the-loop project is one of the projects available.


## Trade-offs and design considerations

### Centralized vs Distributed -->
