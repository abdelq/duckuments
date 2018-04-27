# Modern signal processing {#modern_signal_processing status=draft}

Assigned: Andrea Censi


<div class='requirements' markdown='1'>

Requires: Understanding of time series. See: [](#time-series).

Result: Understanding of the basic concepts of
event-based processing and why it is different from periodic processing.

Results: Understanding of latency, frequency.

</div>

## Event-based processing

The response to these challenges claims the reformulation of answers to fundamental questions referred to discrete-time systems: “when to sample,” “when to update control action,” or “when to transmit information.” XXX

One of the generic answers to these questions is covered by adoption of the event-based paradigm that represents a model of calls for resources only if it is really necessary in system operation. In event-based systems, any activity is triggered as a response to events defined usually as a significant change of the state of relevance. Most “man-made” products, such as computer networks, complex software architectures, and production processes are natural, discrete event systems as all activity in these systems is driven by asynchronous occurrences of events. XXX


## Periodic vs event-based processing

In standard signal processing, the data is assumed to arrive periodically
with a certain fixed interval; in robotics, it is common to work
with streams of data that arrive irregularly.

As per [](#def:time-series-def), a time series is
a sequence $\tup{t_k, x_k} \in \Time \times \aset{X}$, where $\Time$ is
time and $\aset{X}$ is the domain in which the signals take values.

If the time series is periodic, it means that
\[
    t_k = t_0 + \Delta t_k.
\]

Therefore, periodic processing is a special case of event-based processing.

<!-- Event-based processing is thus a generalization of periodic processing. -->

## Why working with events

How

### Sensor-driven processing

The sensor tells the controller when there is interesting data to process.



### Task-driven processing

The controller tells the sensor when to send data.


## Definition of message statistics




### Latency

TODO: to write

### Frequency

TODO: to write

### Jitter

TODO: to write

### Signal reliability

TODO: to write

Some events might be lost, because the network loses the packet.

## On the independence of latency and frequency

Latency and frequency are to be considered two completely independent
quantities.

Here's

## Design considerations and trade-offs

Should you structure your application with periodic processing,
or event-based processing? Here's a few things to keep in mind.

### Need for real-time system

To have truly periodic processing, you need to have an operating
system that is "real-time".

See: [](#RTOS)

A real-time operating system will be able to schedule processing
of data at given intervals.

### Periodic processing is easier to analyze

Periodic processing is easier to analyze from the theoretical
point of view.

### Packet losses vs latency

There are situations where sometimes you prefer to lose packets.

Assumes: k:udp, k:tcp

### Latency

See: [Latency numbers every programmer should know](https://people.eecs.berkeley.edu/~rcs/research/interactive_latency.html)


<!-- ## In Duckietown

### Processing loop of line detection

Processing loop of line detection. Bounded CPU usage. XXX -->


## Further reading

* A reference on all things event-based (control and signal processing) [](#bib:miskowicz2015event)

* A simple discussion of event-based control by K. J. Åström [](#bib:astrom08eventbased)

For a couple of different possible models for event-based
processing:

* Synchronous Data Flow [](#bib:lee87synchronous), in which each
  actor consumes a fixed amount of messages on each port.
* Delta Data Flow [](#bib:manohar10delta)
