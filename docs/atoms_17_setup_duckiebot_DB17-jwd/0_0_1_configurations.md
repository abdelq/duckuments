# Duckiebot configurations {#duckiebot-configurations status=ready}


<div class='requirements' markdown="1">

Requires: nothing

Results: Knowledge of Duckiebot configuration naming conventions, their components and functionalities.

Next steps: After reviewing the configurations, you can proceed to purchasing the components, reading a description of the components, or assembling your chosen configuration.

</div>

We define different Duckiebot configurations depending on their time of use and hardware components. This is a good starting point if you are wondering what parts you should obtain to get started.

<!--
Once you have decided which configuration best suits your needs, you can proceed to the detailed descriptions for [`DB17-wjd`](#acquiring-parts-c0) or [`DB17-wjdlc`](#acquiring-parts-c1) Duckiebot.
-->

## Duckiebot Configurations: Fall 2017

The configurations are defined with a root: `DB17-`, indicating the "bare bones" Duckiebot used in the Fall 2017 synchronized course, and an appendix `y` which can be the union (in any order) of any or all of the elements of the optional hardware set $\aset{O} = \{$`w`, `j`, `d`, `p`, `l`, `c`$\}$.

<!--
A `DB17` Duckiebot can navigate autonomously in a Duckietown, but cannot communicate with other Duckiebots.
-->

The elements of $\aset{O}$ are labels identifying optional hardware that aids in the development phase and enables the Duckiebot to talk to other Duckiebots. The labels stand for:

- `w`: 5 GHz **w**ireless adapter to facilitate streaming of images;

- `j`: wireless **j**oypad that facilitates manual remote control;

- `d`: USB **d**rive for additional storage space;

- `c`: a different **c**astor wheel to _replace_ the preexisting omni-directional wheel;

<!--
- `p`: **P**WM hat for convenient powering of the DC motor hat;
-->

- `l`: includes **L**EDs, LED hat, bumpers and the necessary mechanical bits to set the bumpers in place. Note that the installation of the bumpers induces the _replacement_ of a few `DB17` components;

Note: During the Fall 2017 course, three Duckietown Engineering Co. branches (Zurich, Montreal, Chicago) are using these configuration naming conventions. Moreover, all institutions release hardware to their Engineers in training in two phases. We summarize the configuration releases [below](#duckiebot-releases-2017).

## Configuration functionality

### `DB17` {#duckiebot-configurations-db17}

This is the minimal configuration for a Duckiebot. It is the configuration of choice for tight budgets or when operation of a single Duckiebot is more of interest than fleet behaviors.


- **Functions**: A `DB17` Duckiebot can navigate autonomously in a Duckietown, but cannot communicate with other Duckiebots.


- **Components**: A "bare-bones" `DB17` configuration includes:

<div markdown="1">

 <col2 id='db17' figure-id="tab:db17" figure-caption="Components of the DB17 configuration">
    <s>[Chassis](http://www.kr4.us/magician-chassis-rob-12866.html)</s>                         <s>USD 20</s>
    <s>[Camera with 160-FOV Fisheye Lens](https://tinyurl.com/ybwrcywc)</s>                         <s>USD 22</s>
    <s>[Camera Mount](https://tinyurl.com/ybyewdrt)</s>                         <s>USD 8.50</s>
    <s>[300mm Camera Cable](https://www.adafruit.com/product/1648)</s>                         <s>USD 2</s>
    <s>[Raspberry Pi 3 - Model B](https://tinyurl.com/ycsujzb9)</s>                         <s>USD 35</s>
    <s>[Heat Sinks](https://tinyurl.com/yayj2qen)</s>                         <s>USD 5</s>
    <s>[Power supply for Raspberry Pi](https://www.adafruit.com/product/1995)</s>                         <s>USD 7.50</s>
    <s>[16 GB Class 10 MicroSD Card](https://tinyurl.com/ydawrgdx)</s>                         <s>USD 10</s>
    <s>[Mirco SD card reader](https://www.adafruit.com/product/939)</s><s>USD 6 </s>
    <s>[DC Motor HAT](https://tinyurl.com/y7qurpcw)</s>                         <s>USD 22.50</s>
    <s>[Spliced USB-A power cable](#power-cable-prep-c0)</s>                         <s>USD 0</s>
    <s>[2 Stacking Headers](https://www.adafruit.com/product/2223)</s><s>USD 2.50/piece</s>
    <s>[Battery](https://tinyurl.com/ya7otc76)</s>                         <s>USD 20</s>
    <s>[16 Nylon Standoffs (M2.5 12mm F 6mm M)](https://tinyurl.com/y9uy73b2)</s>                         <s>USD 0.05/piece</s>
    <s>[4 Nylon Hex Nuts (M2.5)](https://tinyurl.com/ydy4znem)</s>                      <s>USD 0.02/piece</s>
    <s>[4 Nylon Screws (M2.5x10)](https://tinyurl.com/ya2uo9so)</s>                     <s>USD 0.05/piece</s>
    <s>[2 Zip Ties (300x5mm)](https://tinyurl.com/yb8v3nns)</s>                         <s>USD 9</s>
    <s>Total cost for `DB17` configuration</s>                         <s>USD 173.6</s>
 </col2>

</div>


- **Description of components**: [](#acquiring-parts-c0)


- **Assembly instructions**: [Without videos](#assembling-duckiebot-c0), [with videos](#assembling-duckiebot-db17-ttic)

### `DB17-w`

This configuration is the same as `DB17` with the _addition_ of a 5 Ghz wireless adapter.


- **Functions**: This configuration has the same functionality of `DB17`. In addition, it equips the Duckiebot with a secondary, faster, Wi-Fi connection, ideal for image streaming.


- **Components**:

<div markdown="1">

 <col2 id='db17-w' figure-id="tab:db17-w" figure-caption="Components of the DB17-w configuration">
    <s>[`DB17`](#duckiebot-configurations-db17)</s>                         <s>USD 173.6</s>
    <s>[Wireless Adapter (5 GHz)](https://tinyurl.com/ycvu7ok3)</s><s>USD 20</s>
    <s>Total cost for `DB17-w` configuration</s>                         <s>USD 193.6</s>
 </col2>

</div>


- **Description of components**: [](#acquiring-parts-c0)


- **Assembly instructions**: [Without videos](#assembling-duckiebot-c0), [with videos](#assembling-duckiebot-db17-ttic)

### `DB17-j`

This configuration is the same as `DB17` with the _addition_ of a 2.4 GHz wireless joypad.


- **Functions**: This configuration has the same functionality of `DB17`. In addition, it equips the Duckiebot with manual remote control capabilities. It is particularly useful for getting the Duckiebot our of tight spots or letting younger ones have a drive, in addition to providing handy shortcuts to different functions in development phase.


- **Components**:


<div markdown="1">

 <col2 id='db17-j' figure-id="tab:db17-j" figure-caption="Components of the DB17-j configuration">
    <s>[`DB17`](#duckiebot-configurations-db17)</s>                         <s>USD 173.6</s>
    <s>[Joypad](https://tinyurl.com/y9klooef)</s>                         <s>USD 10.50</s>
    <s>Total cost for `DB17-j` configuration</s>                         <s>USD 184.1</s>
 </col2>

</div>


- **Description of components**: [](#acquiring-parts-c0)


- **Assembly instructions**: [Without videos](#assembling-duckiebot-c0), [with videos](#assembling-duckiebot-db17-ttic)

### `DB17-d`

This configuration is the same as `DB17` with the _addition_ of a USB flash hard drive.


- **Functions**: This configuration has the same functionality of `DB17`. In addition, it equips the Duckiebot with an external hard drive that is convenient for storing videos (logs) as it provides both extra capacity and faster data transfer rates than the microSD card in the Raspberry Pi. Moreover, it is easy to unplug it from the Duckiebot at the end of the day and bring it over to a computer for downloading and analyzing stored data.


- **Components**:


<div markdown="1">

 <col2 id='db17-d' figure-id="tab:db17-d" figure-caption="Components of the DB17-d configuration">
    <s>[`DB17`](#duckiebot-configurations-db17)</s>                         <s>USD 173.6</s>
    <s>[Tiny 32GB USB Flash Drive](https://tinyurl.com/ycao6men)</s>                         <s>USD 12.50</s>
    <s>Total cost for `DB17-d` configuration</s>                         <s>USD 186.1</s>
 </col2>

</div>


- **Description of components**: [](#acquiring-parts-c0)


- **Assembly instructions**: [Without videos](#assembling-duckiebot-c0), [with videos](#assembling-duckiebot-db17-ttic)

### `DB17-c`

In this configuration, the `DB17` omni-directional wheel is _replaced_ with a caster wheel.


- **Functions**: The caster wheel upgrade provides a smoother ride.


- **Components**:

<div markdown="1">

 <col2 id='db17-c' figure-id="tab:db17-c" figure-caption="Components of the DB17-c configuration">
    <s>[`DB17`](#duckiebot-configurations-db17)</s>                         <s>USD 173.6</s>
    <s>[Caster](https://tinyurl.com/y7gnesxn) (`DB17-c`)</s>                         <s>USD 6.55/4 pieces</s>
    <s>[4 Standoffs (M3 12mm F-F)](https://tinyurl.com/ybd24t8c)</s>                         <s>USD 0.63/piece</s>
    <s>[8 Screws (M3x8mm)](https://tinyurl.com/ych4sfpa)</s>                         <s>USD 4.58/100 pieces</s>
    <s>[8 Split washer lock](https://tinyurl.com/y75onase)</s>                         <s>USD 1.59/100 pieces</s>
    <s>Total cost for `DB17-c` configuration</s>                         <s>USD 178.25</s>
 </col2>

</div>


TODO: update links of mechanical bits from M3.5 to M3.

Note: The omni-directional caster wheel is included in the chassis package, so replacing it does not reduce the `DB17` cost.


- **Description of components**: [](#acquiring-parts-c1)


- **Assembly instructions**: [](#assembling-duckiebot-c1)

### `DB17-l`

In this configuration the Duckiebot in equipped with the necessary hardware for controlling and placing 5 RGB LEDs on the Duckiebot. Differently from previous configurations that add or replace a single component, `DB17-l` introduces several hardware components that are all necessary for a proper use of the LEDs.

It may be convenient at times to refer to hybrid configurations including any of the `DB17-jwcd` in conjunction with a _subset_ of the `DB17-l` components. In order to disambiguate, let the partial upgrades be defined as:

- `DB17-l1`: _adds_ a PWM hat to `DB17`, in addition to a short USB angled power cable and a M-M power wire;
- `DB17-l2`: _adds_ a bumpers set to `DB17`, in addition to the mechanical bits to assemble it;
- `DB17-l3`: _adds_ a LED hat and 5 RGB LEDs to `DB17-l1l2`, in addition to the F-F wires to connect the LEDs to the LED board.

Note: introducing the PWM hat in `DB17-l1` induces a _replacement_ of the [spliced cable](#power-cable-prep-c0) powering solution for the DC motor hat. Details can be found in [](#assembling-duckiebot-c1).


- **Functions**: `DB17-l` is the necessary configuration to enable communication between Duckiebots, hence fleet behaviors (e.g., negotiating the crossing of an intersection). Subset configurations are sometimes used in a standalone way for: (`DB17-l1`) avoid using a sliced power cable to power the DC motor hat in `DB17`, and (`DB17-l2`) for purely aesthetic reasons.


- **Components**:

<div markdown="1">

 <col2 id='db17-l' figure-id="tab:db17-l" figure-caption="Components of the DB17-l configuration">
 <s>[`DB17`](#duckiebot-configurations-db17)</s>                         <s>USD 173.6</s>
     <s>[PWM/Servo HAT](https://tinyurl.com/yd8bdl2r) (`DB17-l1`)</s>   <s>USD 17.50</s>
     <s>[Power Cable](https://tinyurl.com/yaptpssu) (`DB17-l1`)</s><s>USD 7.80</s>                      
     <s>[Male-Male Jumper Wire (150mm)](https://www.adafruit.com/products/1957)  (`DB17-l1`)</s>                         <s>USD 1.95</s>
    <s>[Bumper set]() (`DB17-l2`)</s><s>USD 7 (custom made)</s>
    <s>[8 M3x10 pan head screws](https://www.mcmaster.com/#92005a120/=19lvrzk) (`DB17-l2`)</s><s>USD 7 (custom made)</s>
    <s>[8 M3 nuts](https://www.mcmaster.com/#90591a250/=19lvsom) (`DB17-l2`)</s><s>USD 7 (custom made)</s>
    <s>[Bumpers]() (`DB17-l2`)</s><s>USD 7 (custom made)</s>   
    <s>[LEDs](https://www.adafruit.com/product/848) (`DB17-l3`)</s>                         <s>USD 10</s>
    <s>[LED HAT](https://tinyurl.com/ydh9wqp5) (`DB17-l3`)</s><s>USD 28.20 for 3 pieces</s>
    <s>[20 Female-Female Jumper Wires (300mm)](https://www.adafruit.com/products/793) (`DB17-l3`)</s>         <s>USD 8</s>
    <s>[4 4 pin female header](http://www.digikey.com/product-detail/en/PPTC041LFBN-RC/S7002-ND/810144) (`DB17-l3`)</s><s>USD 0.60/piece</s>
    <s>[12 pin male header](http://www.digikey.com/product-detail/en/amphenol-fci/68000-412HLF/609-3266-ND/1878525) (`DB17-l3`)</s><s>USD 0.48/piece</s>
    <s>[2 16 pin male
    header](http://www.digikey.com/product-detail/en/0022284160/WM50014-16-ND/313801) (`DB17-l3`)</s><s>USD 0.61/piece</s>
    <s>[3 pin male header](http://www.digikey.com/product-detail/en/M20-9990345/952-2263-ND/3728227) (`DB17-l3`)</s><s>USD 0.10/piece</s>
    <s>[2 pin female shunt jumper](http://www.digikey.com/product-detail/en/382811-8/A26228-ND/293121) (`DB17-l3`)</s><s>USD 2/piece</s>
    <s>[40 pin female header](https://www.adafruit.com/products/2222) (`DB17-l3`)</s>                   <s>USD 1.50</s>
    <s>[5 200 Ohm resistors](https://tinyurl.com/yaramn3g) (`DB17-l3`)</s><s>USD 0.10/piece</s>
    <s>[10 130 Ohm resistors](https://tinyurl.com/y9vz2b9v) (`DB17-l3`)</s><s>USD 0.10/piece</s>
    <s>Total for `DB17-l` configuration</s>                         <s>USD 305</s>
 </col2>

</div>


- **Description of components**: [](#acquiring-parts-c1)


- **Assembly instructions**: [](#assembling-duckiebot-c1)


## Branch configuration releases: Fall 2017 {#duckiebot-releases-2017}

All branches release their hardware in two phases, namely `a` and `b`.

### Zurich

- First release (`DB17-Zurich-a`): is a `DB17-wjd`.

- Second release (`DB17-Zurich-b`): is a `DB17-wjdcl`.

### Montreal

- First release (`DB17-Montreal-a`): is a hybrid `DB17-wjd` + PWM hat (or `DB17-wjdl1`).

- Second release (`DB17-Montreal-b`): is a `DB17-wjdl`.

Note: The Montreal branch is not implementing the `DB17-c` configuration.

### TTIC

- First release (`DB17-Chicago-a`): is a `DB17-wjd`.

- Second release (`DB17-Chicago-b`): is a `DB17-wjdl`.

Note: The Chicago branch is not implementing the `DB17-c` configuration.

<!--
<s>Total for `DB17-wjd` configuration</s>                         <s>USD 216.6</s>
-->
