# Demo instructions Fleet Communications {#demo-instruction-fleet-com status=draft}

TODO: JT: fix spelling and grammar, move to operation manual section

This is the description of a communication setup between multiple Duckiebots.

<div class='requirements' markdown="1">

Requires: At least two Duckiebots in configuration DB17-w or higher.

Requires: One additional wireless adapter per Duckiebot and laptop. (e.g. TP-Link TL-WN822N or TL-WN821N).

Requires: A laptop.

</div>

## Duckietown setup notes {#demo-fleetcom-duckietown-setup}

For this Demo, no Duckietown is needed.


For this demo, additional wireless adapters are needed that allow mesh networking (e.g. TP-Link TL-WN822N or TL-WN821N).

## Pre-flight checklist {#demo-fleetcom-pre-flight}

This pre-flight checklist describes the steps that ensure that the installation and demo will run correctly:

Check: The additional Wifi adapter is installed and works.

    $ sudo apt-get install build-essential linux-headers-generic dkms git
    $ git clone https://github.com/Mange/rtl8192eu-linux-driver.git
    $ sudo dkms add ./rtl8192eu-linux-driver
    $ sudo dkms install rtl8192eu/1.0

Check: Duckiebots have sufficient battery charge.

## Demo setup {#demo-fleetcom-setup}
Some packages are needed to enable the communication beween the Duckiebots, namely Protobuf, ZeroMQ and B.A.T.M.A.N.

To install them, ssh into the Duckiebots and source the environment

    $ cd duckietown
    $ source environment.sh

pull the necessary files from devel-distributed-est-master.

Then find the name of the wifi interface you want to use with iwconfig. (eg. wlx7c8bca1120e0).

    $ iwconfig

Next specify a static IP adress and subnet and write it on a piece of paper, be carefull to not use the same IP on two bots. However, the subnet should stay the same on all bots. (eg. 192.168.15.38/24)

Change to dependecie directory

    $ cd ~/duckietown/catkin_ws/src/30-localization-and-planning/fleet_messaging/dependencies

and install everything with one handy script!

    $ ./install_fleet_messaging <wifi-iface> <ipaddr>

Now you need to alter your network config, for this open the interfaces file:

    $ sudo vim /etc/network/interfaces

Change all four instances of wlan0 to wlan1.

After a reboot you are ready to make your Duckiebots talk to each other.


## Demo instructions {sec:demo-fleetcom-instructions}

To run the demo ssh into the bots, then in your duckietown repository run:

    $ source environment.sh

    $ roslaunch fleet_messaging tester.launch

and enjoy the show!

[Demo video](https://drive.google.com/file/d/1zbOqEXugNF9p6Ln8f2nk8CakFrZYiSbp/preview)

## Troubleshooting 

It's networking. If it doesn't work try reinstalling while letting 99 duckies swim in the bathtub and lighting magic candles.

## Demo failure demonstration {#demo-fleetcom-failure}

[terminal_full_of_errors.avi](https://youtu.be/rlpgaGqIupg?t=350s)
