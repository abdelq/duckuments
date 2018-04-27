# Coordinate systems {#coordinate_systems status=beta}

## Motivation

In order to uniquely specify a position in some space, we use some numbers, _coordinates_, in a _coordinate system_. For example, in daily life, we would use the intersection of two streets, each with a unique name in the city, to specify the location of some cafe. If you find yourself in the ocean, you might communicate your location to someone by telling them the latitude and longitude readout on your GPS device. Generally speaking, a coordinate system provides us a way to denote _any_ position in an _unambiguous_ way. So you can communicate any position to another person, and by using the given coordinates, that person can arrive at the same exact position in space. Note, however, different coordinates can correspond to the same point.

## Definitions

\begin{definition}[Coordinate system]\label{def:coordinate_system}
A coordinate system is a surjective function mapping from a tuple of reals to some space $S$, respecting the local topology. (The local topology, which is beyond the scope of this chapter, roughly means that "nearby" points have coordinates "close" together.)
\end{definition}

## Examples

Because the ability of _naming_ or specifying a point in space is so fundamentally important, we often take that coordinates given by some coordinate system, often a Cartesian coordinate system, as the name of the point.

### 1D

Consider the real number line $\reals$ as the space $S$. We can name an arbitrary point $x \in \reals$, which happens to be a real number, by itself. So to check with our definition, any two distinct points on the real line would have two distinct coordinates. Furthermore any point has a coordinate. Let's call this coordinate system $A$.

One should note that the coordinate system given above is not the only possible way to name the points on a real line. We can assign coordinate $-x$ to the point $x \in \reals$ and obtain an equally valid coordinate system $B$. To be more specific, given a point $p$ with the coordinate $a$ in the first coordinate system $A$, we know that in the second coordinate system $B$, $p$ would have the coordinate $-a$. Therefore, there is a way to translate between coordinates in the two systems.

### 2D plane

Consider the real plane $\reals^2$ as the space $S$. This is an important space within robotics and beyond. It can be used to represent images, with each pixel having its own position, or the location of your Duckiebot in Duckietown.

#### 2D Cartesian coordinate systems

We can draw two perpendicular lines on the plane $S$. We call these two lines the $x$-axis and the $y$-axis. We assign $(0, 0)$ to the point of intersection, which we call _the origin_. Then we decide on the positive directions and units for each axis and the unit. We will use coordinates $(x, y)$ to specify a point located $x$-many units in the positive $x$-direction and $y$-many units in the positive $y$-direction away from the origin, respectively. If we draw the axis-parallel lines with _integral_ $x$ coordinate and lines with integral $y$ coordinate, we obtain a visualization similar to that in [](#fig:2d-cartesian).

When representing the location of your Duckiebot in Duckietown, you might decide to choose a corner of the map as the origin and take east as the positive $x$-direction and north as the positive $y$-direction, and 1 meter as the unit length. In this case, a Duckiebot with location $(1, -2)$ would sit at 1 meter east and 2 meters south of the designated corner of the map.

<div figure-id="fig:2d-cartesian" figure-caption="A Cartesian coordinate system in the 2D plane">
     <img src="2d-cartesian.svg" style='width: 15em'/>
</div>

\begin{remark}[Image space]\label{rem:image_space}
It is customary to put the origin of an image at the top-left corner with the $x$-axis being horizontal and increasing to the right and the $y$-axis vertical and increasing downwards. In this way, the $x$ and $y$ coordinates index the column and row, respectively, of a particular pixel in the image. Such a convention is observed in `OpenCV` and other software libraries.
\end{remark}

#### Polar coordinate systems

An alternative coordinate system for the plane is the polar coordinate system, where we specify a point by its direction and distance from a fixed reference point. To set up a polar coordinate system, you first decide on the _pole_, the reference point, then the _polar axis_, the reference direction. We will call the distance from the pole, the _radial coordinate_ or _radius_, commonly denoted by $r$ or $\rho$, and the angle from the polar axis, the _angular coordinate_ or _polar angle_, commonly denoted by $\phi$, $\varphi$ or $\theta$. See an example in [](#fig:2d-polar).

<div figure-id="fig:2d-polar" figure-caption="A polar coordinate system with pole O and polar axis L.">
     <img src="2d-polar.svg" style='width: 15em'/>
</div>

Note that in a polar coordinate system, a point has many equally valid names.

<div class='check' markdown="1">
Exercise to readers: provide two such points and a few of their coordinates each.
</div>

Now, consider a Cartesian coordinate system $C$ whose origin is at the pole and its positive $x$-direction coincides with the polar axis. It is not hard to convert polar coordinates to Cartesian coordinates in $C$.

<div class='check' markdown="1">
Exercise to readers: consult [](#fig:2d-polar-to-cart) and write out the conversion formulae.)
</div>

<div figure-id="fig:2d-polar-to-cart" figure-caption="Converting from polar coordinates to Cartesian coordinates.">
  <img src="2d-polar-to-cart.svg" style='width: 15em'/>
</div>

Given the many options, you might wonder which coordinate system to use in any given situation. The answer is a practical one. Choose the one that helps simplify the problem at hand. As a trivial example, consider the equation for a unit circle. In a Cartesian coordinate system, it would be $x^2 + y^2 = 1$ whereas in a polar coordinate system, it would be much simpler: $r = 1$.

<div class='check' markdown="1">
Exercise to readers: how about the equation for a straight line in polar coordinates?
</div>

### 3D space

This is an important space since we live in a three-dimensional world. Since many of our robots operate in this same world, many robots similarly represent coordinates in three dimensions, including unmanned aerial vehicles (UAVs) and autonomous underwater vehicles (AUVs).

#### 3D Cartesian coordinate systems

Suppose the plane is the page or screen you are reading from, which is just a slice through the 3D space around it,  we can extend a 2D Cartesian coordinate system on the plane to 3D by adding a $z$-axis that is perpendicular to the page, i.e., the $z$-, $x$-, and $y$-axis are mutually perpendicular. As done before, we need to choose a positive $z$-direction and there are two choices: coming out of the page or going into the page. They form the right-handed coordinate system or the left-handed coordinate system, respectively. We shall use right-handed coordinate systems unless otherwise noted. For more on handedness, see [Wikipedia](https://en.wikipedia.org/wiki/Cartesian_coordinate_system#Orientation_and_handedness). Now the resulting coordinates become $(x, y, z)$, see [](#fig:3d-cart).

<div figure-id="fig:3d-cart" figure-caption="A 3D Cartesian coordinate system.">
  <img src="3d-cart.svg" style='width: 15em'/>
</div>

#### Spherical coordinate systems

Similarly, we can extend the polar coordinate systems on the page or screen to 3D by defining a _zenith direction_ (upwards) perpendicular to the plane, the _polar angle_ to be the angle away from zenith, and the _azimuth angle_ to be the orthogonal projection of a point's angle away from the polar axis on the plane. Together, a point has coordinates $(r, \theta, \phi)$ where $\theta$ denotes the polar angle and $\phi$, the azimuth angle. See [](#fig:3d-spherical).

<div class='check' markdown="1">
Exercise to readers: how to convert spherical coordinates to 3D Cartesian coordinates? and back?
</div>

<div figure-id="fig:3d-spherical" figure-caption="A spherical coordinate system.">
  <img src="3d-spherical.svg" style='width: 15em'/>
</div>

## Further reading
 
If you find this topic interesting, there are many more coordinate systems than the ones covered here, such as the:

See also: [cylindrical coordinate system](https://en.wikipedia.org/wiki/Cylindrical_coordinate_system) in 3D space and

See also: [parabolic coordinate system](https://en.wikipedia.org/wiki/Parabolic_coordinates) in 2D space.

Author: Falcon Dai

Maintainer: Falcon Dai
