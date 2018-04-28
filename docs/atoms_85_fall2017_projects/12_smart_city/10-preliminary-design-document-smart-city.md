# Smart city {#part:smart-city}

#  PDD - Smart City {#smartcity-pdd status=beta}


## Part 1: Mission and scope

### Mission statement

Make Duckietown a smarter city.

### Motto

Motto: OMNES VIAE ANATUM URBEM DUCUNT <br/>(All roads lead to Duckietown)



### Project scope

#### What is in scope

* Manufacturing process of tiles
    * Consider different ways to implement the lines on the road
    * Spray tiles for lines instead of tape
* Power Grid
    * Add power to each tile
    * Establish power grid layout
    * Establish power grid design and implementation


#### What is out of scope

* Communication protocol (what to do with the data)
* Appearance specifications redefinition (cit. “we need an Italian architect for this”)
* Traffic controller HUB
* City wide power hub

#### Stakeholders

| Team   | Reference Person |
|----------|-------------|
| Intersection Navigation |  Nicolas Lanzetti (ETHZ) |
| Parking |    Samuel Nyffenegger (ETHZ)   |
| Traffic controller HUB | no teams actively working on this project in Fall-2017 |
|System Architect | Sonja (ETHZ) |
| Software Architect | Breandean (UdM) |
| Knowledge | Tzarina |


## Part 2: Definition of the problem

### Problem statement

We have to design a traffic lights system that integrates seamlessly and efficiently with the tiles currently used to build Duckietown. The development of a traffic lights system has to be considered as part of a bigger plan aimed to make Duckietown a smart city. A smart Duckietown has the capability of delivering wireless connectivity everywhere (Duckietown Wireless Network - DWN) in the town and power to each tile. A tile that can provide power is called a hot tile. The power grid that provides power to all the tiles is called Duckietown Power Grid (DPG). A simple use case for this infrastructure would then be the traffic lights system. Traffic lights at each intersection are powered and controlled by a Raspberry Pi with a Duckiebot-like LED Hat and 3 (or 4) LEDs. A Raspberry Pi responsible for the traffic lights at an intersection draws power from a hot tile and connects to the DWN.

### Terminology

* DWN: Duckietown Wireless Network
* DPG: Duckietown Power Grid
* PD: Powered Device

### Assumptions

* 2 traffic light per current city design (1 at 4-way the other at 3-way intersection)
* Appearance specifications are given and must be respected
* There exists a Duckietown Wireless Network (DWN) that any wifi enabled device placed within the town can connect to (e.g. traffic lights).
* There is access to power source close to Duckietown that can power the power grid

### Approach

To create a smarter Duckietown and provide data and power to the tiles, we will wireless networks (e.g., WiFi, Bluetooth, etc.) for data communication, and we will implement a power grid to provide power to the various devices and PDs throughout Duckietown. Since we are using common implementation of wireless networks, the rest of this design document will focus on the specifications of the power grid.


**Power Grid Implementation Ideas:**

* Idea 1: Attach a 2-row breadboard along the edges of each tile, between the white tape and the teeth of the tile. PDs are connected to the power grid simply by inserting the two wires (+ and -) into the relative holes.
    * Problems: The primary problem under this approach is that breadboards are rated for only ~1amp, which is not nearly enough power needed for the power grid (for example, a single Raspberry Pi can use more power than that. This problem essentially eliminates the feasibility of this idea for the DPG.


* Idea 2: Attach a plastic rail to the edge of each tile, between the white tape and the teeth of the tile. The rail would carry two conductive strips (copper strips), one on each side (see image below).
    * Prototype: The image below shows a possible design of the plastic rail along with a compatible plug. The black part of the 3D model above constitutes the rail (sectional view) while the white part is the plug. The system is designed so that the plug, once pressed onto the rail, remains attached. The white box on the plug would contain one of the step-down converters (http://a.co/fAIAhuw) described above. This would solve the problem of having a weak 5V power grid by running 24V through the grid and stepping it down to 5V only when, and exactly where, we need it. There would be limit neither to the number of plugs nor to the position where we can attach them (even better than a breadboard in this sense).
We can then design simple connectors for straight and curved tiles to make everything modular.
Since the most common PD in Duckietown is a Raspberry Pi, we can design a USB plug (shown below) to make things even easier.

    * Enhancement 1: We can modify the plug by adding an extrusion to one side and carving its negative into the rail. This would prevent us from attaching the plug in the wrong direction, thus violating the positive/negative polarity of the conductors.
    * Enhancement 2: Since the plastic material used by 3D printers is usually inflexible we can change the plug such that the plastic does not follow the design of the rail (i.e., it would look like a U flipped upside-down) and have a curved copper strip that stretches when the plug is pushed onto the rail and loosens when the plug sits completely on the rail. Basically, it follows the same concept used in the classic cigarette lighter plug present in a vehicle.
    * Enhancement 3: We can use plastic T-slotted extrusion elements and design a plug that works with them.
Problem: The primary problem with this approach is its difficult, especially given the project’s short timeframe. However, we could focus on designing and building a prototype that works that could then be mass produced and implemented for the whole Duckietown sometime in the future.


![Plug 1](plug1.jpg)
![Plug 2](plug2.png)
![Plug 3](plug3.png)


* Idea 3: Have the connectors between tiles also serve as the output location for power to the tile. Use audio cable or RCA cable for the power rails and connect them at the corners of the tile using a 3 way connector, such as those shown below. This approach solves the issue regarding gendering the connectors and providing power nodes to the city. Cheap and easy to mass produce.
    * Problem: This may require modification of the tiles, such as removing one of the interlocking teeth to allow for the connector.

![Plug 4](plug4.png)
![Plug 5](plug5.png)

### Functionality-resources trade-offs

### Functionality provided

The actual voltage and amperage available at each tile/power terminal will depend on the power grid approach we choose. Regardless of the implementation, the primary functionality provided by the power grid is access to power for at each tile in the Duckietown.

### Resources required / dependencies / costs
The resources for this project are the parts to build the traffic lights and the power grid. Since, the specific parts and associated costs for the power grid are highly dependent on the implementation approach we decide on, we are unable to obtain specific details at this time. However, for all of the approaches, we will need enough parts to build a power grid that provides power for all of the tiles in the Duckietown.

### Performance measurement

Power Grid:

* Maximum number of powered devices per tile
* Ease of assembly/disassembly
* Ease of manufacturing
* How robust is the power grid under normal usage

System:

* Maximum image frame-rate traffic lights can sustain over the utilities network (network bandwidth)


## Part 3: Preliminary design

### Modules

* Laying the power cables
* Connecting the power cables
* Output power for tile


### Interfaces
Input: 12/24 V, Output: 12/24 V between tiles, 5 V on tile

### Preliminary plan of deliverables

Power grid and integration into the individual tiles must be designed and implemented. While the traffic lights exist, there needs to be a revised method of providing power.

### Specifications

May have to modify Duckietown tiles.

### Software modules

None, this is a hardware project.

### Infrastructure modules

All modules are infrastructure.

## Part 4: Project planning

### First Steps for the next phase
Decide connector option and wire routing.

### Data collection
Stability of power grid. How many traffic lights can be supported per voltage source.

### Data annotation
None.

### Relevant Duckietown resources to investigate
Specification of traffic light.

### Other relevant resources to investigate

None.

### Risk analysis

What could go wrong?

* Wire gauge too low to accommodate power load, causing shorts and possibly melting tiles or starting small fires.
* Live wires are exposed and come into human contact.

How to mitigate the risks?

* Appropriately fuse the tiles and use appropriate wires for power load.
* Insulate everything well and keep open contacts small and covered.
