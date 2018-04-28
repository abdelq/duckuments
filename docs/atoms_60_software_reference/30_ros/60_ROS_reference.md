# ROS installation and reference {#introduction_to_ros status=ready}

Assigned: Liam


## Install ROS {#install-ROS}

This part installs ROS. You will run this twice, once on the laptop, once on the robot.

The first commands are copied from [this page][ros-ubuntu].

[ros-ubuntu]: http://wiki.ros.org/kinetic/Installation/Ubuntu

Tell Ubuntu where to find ROS:

    $ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

Tell Ubuntu that you trust the ROS people (they are nice folks):

    $ sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116

Fetch the ROS repo:

    $ sudo apt update

Now install the mega-package `ros-kinetic-desktop-full`.

    $ sudo apt install ros-kinetic-desktop-full

There's more to install:

    $ sudo apt install ros-kinetic-{tf-conversions,cv-bridge,image-transport,camera-info-manager,theora-image-transport,joy,image-proc,compressed-image-transport,phidgets-drivers,imu-complementary-filter,imu-filter-madgwick}

Note: Do not install packages by the name of `ros-X`, only those by
the name of `ros-kinetic-X`. The packages `ros-X` are from another version of ROS.

XXX: not done in aug20 image:

Initialize ROS:

    $ sudo rosdep init
    $ rosdep update


## `rqt_console` {#rqt_console status=draft}

TODO: to write


## `roslaunch` {#roslaunch status=draft}

TODO: to write

## `rviz` {#rviz status=draft}

TODO: to write

## `rostopic` {#rostopic status=draft}

TODO: to write

### `rostopic hz`

TODO: to write

### `rostopic echo`

TODO: to write

## `catkin_make` {#catkin_make status=draft}

TODO: to write

## `rosrun` {#rosrun status=draft}

TODO: to write

## `rostest` {#rostest status=draft}

TODO: to write

## `rospack` {#rospack status=draft}

TODO: to write

## `rosparam` {#rosparam status=draft}

TODO: to write

## `rosdep` {#rosdep status=draft}

TODO: to write

## `roswtf` {#roswtf status=draft}

TODO: to write

## `rosbag` {#rosbag status=draft}

A bag is a file format in ROS for storing ROS message data. Bags, so named
because of their .bag extension, have an important role in ROS.
Bags are typically created by a tool like
[`rosbag`](http://wiki.ros.org/rosbag/Commandline), which subscribe to one or
more ROS topics, and store the serialized message data in a file as it is received.
These bag files can also be played back in ROS to the same topics they were
recorded from, or even remapped to new topics.

### `rosbag record`

The command
[`rosbag record`](http://wiki.ros.org/rosbag/Commandline#record)
records a bag file with the contents of specified topics.


### `rosbag info`

The command
[`rosbag info`](http://wiki.ros.org/rosbag/Commandline#info)
summarizes the contents of a bag file.


### `rosbag play`

The command
[`rosbag play`](http://wiki.ros.org/rosbag/Commandline#play)
plays back the contents of one or more bag files.


### `rosbag check`

The command
[`rosbag check`](http://wiki.ros.org/rosbag/Commandline#check)
determines whether a bag is playable in the current system, or if it can be migrated.

### `rosbag fix`

The command
[`rosbag fix`](http://wiki.ros.org/rosbag/Commandline#fix)
repairs the messages in a bag file so that it can be played in the current system.

### `rosbag filter`

The command
[`rosbag filter`](http://wiki.ros.org/rosbag/Commandline#filter)
converts a bag file using Python expressions.

### `rosbag compress`

The command
[`rosbag compress`](http://wiki.ros.org/rosbag/Commandline#compress)
compresses one or more bag files.

### `rosbag decompress`

The command
[`rosbag decompress`](http://wiki.ros.org/rosbag/Commandline#decompress)
decompresses one or more bag files.

### `rosbag reindex`

The command
[`rosbag reindex`](http://wiki.ros.org/rosbag/Commandline#reindex)
re-indexes one or more broken bag files.


## `roscore` {#roscore status=draft}

TODO: to write


## Troubleshooting ROS {#troubleshooting-ROS}

Symptom: `![computer] is not in your SSH known_hosts file`

See [this thread][known_host]. Remove the `known_hosts` file and make sure you
have followed the instructions in [](#ssh-local-configuration).

[known_host]: https://answers.ros.org/question/41446/a-is-not-in-your-ssh-known_hosts-file/


## Other materials about ROS.

See also: [A gentle introduction to ROS](https://cse.sc.edu/~jokane/agitr/)
