# Reference frames {#reference_frames status=beta}

<div class="check" markdown="1">
Required Reading: The following assumes a working familiarity with 2D and 3D Cartesian coordinate systems. If you are not familiar with Cartesian coordinate systems, please read the [chapter on coordinate systems](#coordinate_systems).
</div>

## Motivation

Does Earth move around the sun or does the sun move around Earth? It turns out that this is an ill-posed question until we specify a _frame of reference_ for measurement. For us, observers on Earth, it appears that the sun is moving. But for an observer on the moon, both Earth and the sun are moving. In general, motions are relative and we need a reference when measuring motion.

## Definition

A _reference frame_, or just _frame_, is an abstract coordinate system and the set of physical reference points that uniquely specify the coordinate system (location of the origin and orientation). As a way of specifying the reference frame, we often say object $A$ is moving _relative to_ object $B$, instead of specifying explicitly a reference frame $F_B$ that is attached to object $B$.

## Example

Suppose there are two cars A and B both moving at 60 miles per hour eastward. When saying this, we implicitly assume the reference frame of the ground. In the ground's reference frame, the ground itself is at rest, car A and car B are both moving at 60 miles per hour eastward. In car A's reference frame, however, car B is at rest and the ground is _moving_ 60 miles per hour westward!

## Translating motions in one frame to another

To simplify the following discussion, we additionally assume that we choose reference frames such that their axes are parallel. In order to translate motions between reference frames, we assume two rules.

- Relative motions are equal in magnitude and opposite in direction. If frame $R$ is moving relative to frame $S$ at $\avec{u}$, then frame $S$ is moving at $-\avec{u}$ relative to $R$.
- Motions are additive. If a frame $T$ is moving at $\avec{u}$ relative to frame $S$, and frame $S$ is moving at $\avec{v}$ relative to frame $R$, then frame $T$ is moving at $\avec{u} + \avec{v}$ relative to frame $R$.

<div class='check' markdown="1">
Exercise to readers: derive these rules from kinematics.
</div>

As a corollary to the first rule, we immediately derive that frame $R$ is at rest relative to itself, since $\avec{0}$ is the only vector is also its own opposite.

<div class='check' markdown="1">
Exercise to readers: translate car B's motion relative to the ground to relative to car A.
</div>

Author: Falcon Dai

Maintainer: Falcon Dai
