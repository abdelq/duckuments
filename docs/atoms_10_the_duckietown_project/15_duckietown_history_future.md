# Duckietown history and future {#duckietown-history-and-future status=beta}

## The beginnings of Duckietown

The original Duckietown class was at MIT in 2016 ([](#fig:MIT-class)).

<div figure-id="fig:MIT-class">
    <img src="duckietown-mit.jpg" class='fancybox group-photo'/>
    <figcaption>Part of the first MIT class, during the final demo.</figcaption>
</div>

Duckietown was built by elves ([](#fig:elves)).

<div figure-id="fig:elves">
    <figcaption>The elves of Duckietown</figcaption>
    <dtvideo src="vimeo:149916365"/>
</div>

These are some advertisement videos we used.

<div figure-id="fig:v1">
    <figcaption>The need for autonomy</figcaption>
    <dtvideo src="vimeo:152233002"/>
</div>

<div figure-id="fig:v2">
    <figcaption>Advertisement</figcaption>
    <dtvideo src="vimeo:152499589"/>
</div>

<div figure-id="fig:v3">
    <figcaption>Cool Duckietown by night</figcaption>
    <dtvideo src="vimeo:152825632"/>
</div>





## University-level classes in 2016 {status=beta}

Later that year, the Duckietown platform was also used in these classes:

- [National Chiao Tung University 2016](#2016-NCTU), Taiwan - Prof. Nick Wang;
- [Tsinghua University](#2016-Tsinghua), People's Republic of China - Prof. (Samuel) Qing-Shan Jia's *Computer Networks with Applications* course;
- [Rennselaer Polytechnic Institute 2016](#2016-RPI) - Prof. John Wen;

<div figure-id="fig:NCTU">
   <img src="duckietown-taiwan.jpg" class='group-photo'/>
   <figcaption>Duckietown at NCTU in 2016</figcaption>
</div>

<style>
.group-photo {
    max-width: 80%;
}
</style>

## University-level classes in 2017

In 2017, these four courses will be taught together, with the students interacting among institutions:

- [ETH Zürich 2017](#2017-ETHZ) - Prof. Emilio Frazzoli, Dr. Andrea Censi;
- [University of Montreal, 2017](#2017-UdM) - Prof. Liam Paull;
- [TTI/Chicago 2017](#2017-TTIC) - Prof. Matthew Walter; and
- National Chiao Tung University, Taiwan - Prof. Nick Wang.

Furthermore, the Duckietown platform is used also in the following universities:

- Rennselaer Polytechnic Institute (Jeff Trinkle)
- National Chiao Tung University, Taiwan - Prof. Yon-Ping Chen's *Dynamic system simulation and implementation* course.
- Chosun University, Korea - Prof. Woosuk Sung's course;
- Petra Christian University, Indonesia - Prof. Resmana Lim's *Mobile Robot Design Course*
- National Tainan Normal University, Taiwan - Prof. Jen-Jee Chen's *Vehicle to Everything* (V2X) course; and
- Yuan Zhu University, Taiwan - Prof. Kan-Lin Hsiung's Control course.

## Chile  {status=draft}

TODO: to write

## Duckietown High School {status=beta}

### Introduction

DuckietownHS is inspired by the Duckietown project and targeted for high schools.  The goal is to build and program duckiebots capable of moving autonomously on the streets of Duckietown. The technical objectives of DuckietownHS are simplified compared to those of the  Duckietown project intended for universities so it is perfectly suited to the technical knowledge of the classes involved. The purpose is to create self-driving DuckiebotHS vehicles which can make choices and move autonomously on the streets of Duckietown, using sensors installed on the vehicles and special road signs positioned within Duckietown.

Once DuckiebotHS have been assembled and programmed to meet the specifications contained in this document and issued by the "customer" Perlatecnica, special missions and games will be offered for DuckiebotHS. The participants can also submit their own missions and games.

Just like the university project, DuckietownHS is an open source project, a role-playing game, a means to raise awareness on the subject and a learning experience for everyone involved. The project is promoted by the non-profit organization [Perlatecnica][perlatecnica] based in Italy.

[perlatecnica]: http://www.perlatecnica.it

### Purpose

The project has two main purposes:

-   It is a course where students and teachers take part in a role play and they take the typical professional roles of an engineering company. They must design and implement a Duckietown responding to the specifications of the project, assemble DuckiebotHS (DBHS), and develop the software that will run on them. The deliverables of the project will be tutorials, how-to, source code, documentation, binaries and images and them will be designed and manufactured according to the procedures of the DTE.   
-   In respect of that mentioned above, special missions and games for DBHS will be introduced by the "customer" Perlatecnica.

### Perlatecnica's role

Perlatecnica assumes the role of the customer and commissions the Duckietown Engineering company to design and construct the Duckietown and DuckiebotHS. It will provide all necessary product requirements and will assume the responsibility to validate the compliancy of all deliverables to the required specifications.

### The details of the project

The project consists in the design and realization of DuckiebotHS and DuckietownHS. They must have the same characteristics as the city of the University project as far as the size and color of the delimiting roadway bands is concerned but with a different type of management of the traffic lights system that regulates the passage of DuckiebotHS at intersections. The DuckietownHS (DTHS) and DuckiebotHS (DBHS) are defined in the documentation and there is little room for the DTE to make its own choices in terms of design. The reason for this is that the DBHS produced by the different DTE’s need to be identical from a hardware point of view so that the software development makes the difference.

### Where to start

The purchase of the necessary materials is the first step to take. For both DTHS and DBHS a list of these materials is provided with links to possible sellers. Even though Amazon is typically indicated as a seller this is nothing more than an indication to facilitate the purchase for those less experienced. It is left to the individual DTE to choose where to buy the required parts. It is allowed to buy and use parts that are not on the list but this is not recommended as they will make the Duckiebot unfit to enter in official competitions. When necessary an assembly tutorial will be provided together with the list of materials. Once the DTHS city and the DBHS robots have been assembled, the next step will be the development of the software for the running of both the city and the DuckiebotHS.  The city and the Duckiebot run on a board based on a microcontroller STM32 from STMicroelectronics the Nucleo F401RE that will be programmed via the online development environment mbed. Perlatecnica will not release any of the official codes necessary for the navigation of the DuckiebotHS as these are owned by the DTE who developed them. The full standard document is available on the project official web site.   

Each DTE may release the source code under a license Creative Commons CC BY-SA 4.0.

### The first mission of the Duckiebot

Once you have completed the assembly of all the parts that make up the Duckietown and DuckiebotHS you should start programming the microcontroller so that the Duckiebot can move independently.

The basic mission of the DuckiebotHS is to move autonomously on the roads respecting the road signs and traffic lights, choosing a random journey and without crashing into other DuckiebotHS.

For the development of the code, there are no architectural constraints, but we recommend proceeding with order and to focus primarily on its major functions and not on a specific mission.

The main functions are those of perception and movement.

Moving around in DuckietownHS, the DuckiebotHS will have to drive on straight roads, make 90 degree curves while crossing an intersection but also make other unexpected curves. While doing all this the Duckiebot can be supported by a gyroscope that provides guidance to the orientation of the vehicle. 



