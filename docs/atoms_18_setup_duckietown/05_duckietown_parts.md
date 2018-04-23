# Duckietown parts {#duckietown_parts status=draft}

Duckietowns are the cities where Duckiebots drive. Here, we provide a link to all bits and pieces that are needed to build a Duckietown, along with their price tag. Note that while the topography of the map is highly customable, we recommend using the components listed below. Before purchasing components for a Duckietown, read [](#duckietown-specs) to understand how Duckietowns are built.

In general, keep in mind that:

- The links might expire, or the prices might vary.
- Shipping times and fees vary, and are not included in the prices shown below.
- Substitutions are probably not OK, unless you are OK in writing some software.


<div class='requirements' markdown="1">

Requires: Cost (per $m^2$): USD ??? + Shipping Fees

Requires: Time: ??? days (average shipping time)

Results: A kit of parts ready to be assembled in a Duckietown.

Next Steps: [Assembling](#duckietown-assembly) a Duckietown.

</div>

TODO: Figure out costs

## Bill of materials

[//]: #   (test comment)

<div markdown="1">
 <col2 id='materials-duckietown' figure-id="tab:materials-duckietown" figure-caption="Bill of materials for Duckietown">
    <s>[Duckies](https://tinyurl.com/yavv867z)</s>                         <s>USD 17/100 pieces</s>
    <s>[Floor Mats](https://www.walmart.com/ip/Marcy-Classic-24-sq-ft-Floor-Guard-MAT-39/17272585)</s>                      <s>USD 37.5/6 pieces (24 sqft)</s>
    <s>[Duct tape - Red](https://tinyurl.com/ybyc8qrq)</s>                       <s>USD 8.50/roll</s>
    <s>[Duct tape - White](https://tinyurl.com/ydhtzjb4)</s>                       <s>USD 8.50/roll</s>
    <s>[Duct tape - Yellow](http://www.identi-tape.com/duct-tape1.html)</s>               <s>USD 8/roll</s>
    <s>[Traffic signs](https://tinyurl.com/y7nh3ayz)</s>                         <s>USD 18.50/13 pieces</s>
    <s>Total for $\text{Duckietown}/m^2$</s>                         <s>USD ??</s>
 </col2>

TODO: Add suggestions for "small", "medium", "big" towns as a function of $m^2$ and supported bots

</div>

<style>
#materials {
    font-size: 80%;
}
#materials TD {
    text-align: left;
}
</style>

## Duckies

Duckies ([](#fig:duckies)) are essential yet non functional.

<div figure-id="fig:duckies" figure-caption="The Duckies">
     <img src="duckies.png" style='width: 15em'/>
</div>

## Floor Mats

The floor mats ([](#fig:floor-mats)) are the ground on which the Duckiebots drive.

We choose these mats because they have desirable surface properties, are modular, and have the right size to be [street segments](#duckietown-specs). Each square is (~61x61cm) and can connect on every side of other squares. There are 6 mats in each package.

<div figure-id="fig:floor-mats" figure-caption="The Floor Mats">
     <img src="floor-mats.png" style='width: 15em'/>
</div>

Each mat can be a segment of road: straight, a curve, or an intersection (3, or 4 way). To design your Duckietown, see [](#duckietown-specs).

## Duck Tape

We use duck (duct) tape of different colors ([](#fig:all-tapes)) for defining the roads and their signals. White indicates the road boundaries, yellow determines lane boundaries and red are stop signs.

The white and red tape we use are 2 inches wide, while the yellow one is 1 inch wide.

<div figure-id="fig:all-tapes" figure-caption="The Duck Tapes">
     <img src="all-tapes.png" style='width: 15em'/>
</div>

To verify how much tape you need for each road segment type, see [](#duckietown-specs).

[//]: # (per sqm, or per straight mat, curve mat, intersection mat, etc.)

## Traffic Signs

Traffic signs ([](#fig:signs)) inform Duckiebots on the map of Duckietown, allowing them to make driving decisions.

<div figure-id="fig:signs" figure-caption="The Signs">
     <img src="signs.png" style='width: 15em'/>
</div>

Depending on the chosen road topograhy, the number of necessary road signal will vary. To design your Duckietown, see [](#duckietown-specs). You will also need to print out and the signs that you will need as described in [](#signage).

## Traffic lights Parts {#traffic-lights-parts status=draft}

Traffic lights regulate intersections in Duckietown. Here, we provide a link to all bits and pieces that are needed to build a traffic light, along with their price tag. You will need one traffic per either three, or four way intersections. The components listed below meet the appearence specifications described in [](#duckietown-specs).


In general, keep in mind that:

- The links might expire, or the prices might vary.
- Shipping times and fees vary, and are not included in the prices shown below.
- Substitutions are probably OK, if you are willing to write some software.


<div class='requirements' markdown="1">

Requires: Cost: USD ??? + Shipping Fees

Requires: Time: ??? days (average shipping time)

Results:  A kit of parts ready to be assembled in a traffic light.

Next Steps: [Assembling](#traffic-light-assembly) a traffic light.
</div>

TODO: Estimate time and costs

### Bill of materials
 
<div markdown="1">
 <col2 id='materials-traffic-light' figure-id="tab:materials-traffic-light" figure-caption="Bill of materials for traffic light">
    <s>Raspberry Pi</s>                         <s>USD ??</s>
    <s>4 LEDs</s>                         <s>USD ??</s>
    <s>Wires</s>                         <s>USD ??</s>
    <s>Total for Traffic Light</s>                         <s>USD ??</s>
 </col2>

TODO: Complete table

</div>

<style>
#materials-traffic-light {
    font-size: 80%;
}
#materials-traffic-light td {
    text-align: left;
}
</style>

### Raspberry Pi

 ([](#fig:placeholder)) are essential yet non functional.

<div figure-id="fig:placeholder" figure-caption="The placeholder">
     <img src="placeholder.png" style='width: 15em'/>
</div>
