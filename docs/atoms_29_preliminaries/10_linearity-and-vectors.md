# Linearity and Vectors {#linear_algebra status=draft}

Assigned: Jacopo

<!--Start with a brief introduction of the discussed topic, describing its place in the bigger picture, justifying the reading constraints/guidelines below. Write it as if the reader knew the relevant terminology. -->

Linear algebra provides the set of mathematical tools to (a) study linear relationships and (b) describe linear spaces. It is a field of mathematics with important ramifications.

Linearity is an important concept because it is powerful in describing the input-output behavior of many natural phenomena (or _systems_). As a matter of fact, all those systems that cannot be modeled as linear, still can be approximated as linear to gain an intuition, and sometimes much more, of what is going on.

So, in a way or the other, linear algebra is a starting point for investigating the world around us, and Duckietown is no exception.

Note: This chapter is not intended to be a comprehensive compendium of linear algebra.

See: this reference

See also: this other reference

TODO: add references throughout all chapter

<div class='requirements' markdown="1">

Requires: Real numbers are complex for you?: Number theory [addref]()

Requires: $\forall$ is a typo for A and $\in$ are Euros? [Mathematical symbolic language](k:basic-math-notation).

</div>

<!--(Dear Santa, I would like class='recommended-preliminaries' here)
<div class="requirements" markdown="1">

Suggested Reading: Insert here a list of topics and suggested resources related to _recommended_ knowledge in order to better understand the content presented. Example:

Recommended: Definitions of Stability, Performances and Robustness: [](#bib:placeholder), ...

</div>
-->

## Linearity {#linearity}

In this section we discuss vectors, matrices and linear spaces along with their properties.

Before introducing the these arguments, we need to formally define what we mean by linearity. The word _linear_ comes from the latin _linearis_, which means _pertaining to or resembling a line_. You should recall that a line can be represented by an equation like $y = mx + q$, but here we intend linearity as a property of maps, so there is a little more to linearity than lines (although lines _are_ linear maps indeed).

To avoid confusions, let us translate the concept of linearity in mathematical language.

<!-- First, we define a _function_, as a mapping between _sets_.

\begin{definition}[Set]\label{def:set}
A set $\aset{X} = \{x_1, x_2, \dots\}$ is a well-defined collection of distinct _elements_, or _members_ of the set, $x_i$, $i = 1, 2, \dots$. For the time being, we assume elements to be numbers.
\end{definition}

\begin{definition}[Function]\label{def:function}
A function $f : \aset{X} \rightarrow \mathbb{Y}$ is a mapping between the sets $\aset{X}$ and $\mathbb{Y}$. For every input element $x \in \aset{X}$, the mapping will produce an output $y = f(x) \in \mathbb{Y}$.
\end{definition}

<div class="requirements" markdown="1">

Recommended: Functions can be classified by the nature of the relationship between inputs and outputs in: _injective_, _surjective_ or _bijective_ [add-ref]().

</div>
 TODO: add references
-->

<!--<div id='def:function' class="definition latex_env" markdown="1">

A function $f : \aset{X} \rightarrow \mathbb{Y}$ is a mapping between the spaces $\aset{X}$ and $\mathbb{Y}$. For every input element $x \in \aset{X}$, the mapping will produce an output $y = f(x) \in \mathbb{Y}$.

</div> -->

\begin{definition}[Linearity]\label{def:linearity}
A function $f: \aset{X} \to \aset{Y}$ is linear when, $\forall x_i \in \aset{X}$, $i = \{1,2\}$, and $\forall a \in \reals$:

\begin{align}
f(ax_1) &= af(x_1), \label{eq:lin1} \quad \text{and:} \\
f(x_1 + x_2) &= f(x_1) + f(x_2) \label{eq:lin2}
\end{align}

\end{definition}

Condition \eqref{eq:lin1} is referred to as the property of _homogeneity_ (of order 1), while condition \eqref{eq:lin2} is referred to as _additivity_.

\begin{remark}[Superposition Principle]\label{rem:lin-superposition}
Conditions \eqref{eq:lin1} and \eqref{eq:lin2} can be merged to express the same meaning through:
\begin{align}
f(ax_1 + bx_2) = af(x_1) + bf(x_2), \forall x_i \in \aset{X}, i = \{1,2\}, \forall a,b \in \reals \label{eq:linearity}.
\end{align}
\end{remark}

This equivalent condition \eqref{eq:linearity} is instead referred to as _superposition principle_, which unveils the bottom line of the concept of linearity: adding up (equivalently, scaling up) inputs results in an added up (equivalently, scaled up) output.


## Vectors {#theory-chapter-template-notions}

Let $n$ belong to the set of natural numbers $\nats$, i.e., $n \in \nats$, and let $a_i \in \reals$, $i = \{1, \dots, n\}$ be real coefficients. While $\reals$ is the set of real numbers, $\reals^n$ is the set of all $n$-tuples of real numbers.

\begin{definition}[Vector and components]\label{def:vector}

An $n$-dimensional $\textit{vector}$ is an $n$-tuple:

\begin{align} \label{eq:vector}
\avec{v} = \left[ \begin{array}{c} v_1 \\ \vdots \\ v_n \end{array} \right] \in \reals^{n \times 1} \equiv \reals^n,
\end{align}

of _components_ $v_1, \dots, v_n \in \reals$.

\end{definition}

\begin{remark}[Vector notation] \label{rem:vec-tuple-notation}
A more general notation for tuples can be used when denoting vectors:
\begin{align} \label{eq:vector-tuple-notation}
\avec{v} = \tup{v_1, \cdots, v_n}.
\end{align}
In these preliminaries, we will adopt the \eqref{eq:vector} "engineering" notation as it arguably simplifies remembering vector-matrix operations ([](#mats-and-vecs)).
\end{remark}

You can imagine a vector [](#fig:vector-breakdown) as a "directional _number_", or an arrow that starts a certain point and goes in a certain direction (in $\reals^n$). In this representation, the _number_ is the length of the arrow, or the _magnitude_ of the vector (sometimes referred to even as _modulus_), and it can be derived through the vector's components.

\begin{definition}[Length of a vector]\label{def:vec-2-norm}
We define the length, or _modulus_, of a vector $\avec{v} \in \reals^n$ as:
\begin{align} \label{eq:vec-2-norm}
\|\avec{v}\| = \sqrt{v_1^2 + \dots + v_n^2} \in \reals.
\end{align}
\end{definition}

\begin{remark}[2-norm]\label{rem:2norm}
Generally speaking, it is not always possible to define the length of a vector ([addref]()). But when it is possible (e.g., in [Hilbert spaces]()), and in Duckietown it always is, there are many ways to define it. The most common and intuitive definition is the _Euclidian-_ or _2-norm_, which is defined above in \eqref{eq:vec-2-norm}.
\end{remark}

We will discuss norms more in detail in [](#intro-norms).

\begin{definition}[Unit vector]\label{def:unit-vector}
A unit vector, or _versor_, is a vector $\avec{e}$ of of unit length:
\begin{align} \label{eq:unit-vector}
\|\avec{e}\| = 1.
\end{align}
\end{definition}

Unit vectors are used to define the directions of the components of a vector, allowing for an algebraic rather than vectorial representation. As we will see in [](#vector-algebra), this will make the algebra of vectors more intuitive.

<div figure-id="fig:vector-breakdown" figure-caption="A vector, its components expressed as multiples of unit vectors.">
     <img src="placeholder.png" style='width: 15em'/>
</div>

<div class="example-usage" markdown="1">

Let $\avec{v} \in \reals^3$ be a vector defined in the Cartesian space. Let, moreover, $(\avec{i},\avec{j},\avec{k})^T$ be the versor of the Cartesian axis, i.e.:
\begin{align}\label{eq:example-vector-algebraic}
\avec{i} &= [1,0,0]^T; \\
\avec{j} &= [0,1,0]^T; \\
\avec{k} &= [0,0,1]^T.
\end{align}
Then, a vector can be written equivalently in vector or algebraic form: $\avec{v} = [v_1, v_2, v_3]^T = v_1\avec{i} + v_2\avec{j}+v_3\avec{k}$. Unit vectors are sometimes explicitly denoted with a hat (`^`), e.g., $\hat{\avec{i}}, \hat{\avec{j}}, \hat{\avec{k}}$.

</div>

\begin{remark}[Normalizing vectors]\label{rem:vector-normalizing}
Every vector can be made into a unit vector, or _normalized_, by dividing each of its components by the vector's magnitude:
\begin{align}\label{eq:vector-normalizing}
\hat{\avec{v}} = \frac{\avec{v}}{\|\avec{v}\|} = \left[\frac{v_1}{\|\avec{v}\|}, \frac{v_2}{\|\avec{v}\|}, \frac{v_3}{\|\avec{v}\|}\right]^T.
\end{align}
\end{remark}


### Vector algebra {#vector-algebra}

We here define operations amongst two given vectors defined in the same space: $\avec{u} = [u_1, u_2, u_3]^T, \avec{v} = [v_1, v_2, v_3]^T \in \reals^3$.

#### Vectorial Sum {#vector-sum}

The sum of two vectors is a vector, and its components are the sum of the two vectors components.

\begin{definition}[Vectorial sum]\label{def:vector-sum}
\begin{align} \label{eq:vector-sum}
\avec{u} + \avec{v} = [u_1+v_1, u_2+v_2, u_3+v_3]^T.
\end{align}
\end{definition}

\begin{remark}[Sum]\label{rem:sum}
Mathematical operations come in pairs, which represent the same concept. A _sum_ operation, sometimes more extensively referred to as the _algebric sum_, is the concept of summing, i.e., it includes both addition and subtraction. (A subtraction is nothing but an addition between positive and negative numbers.)
\end{remark}

The parallelogram law helps visualize the results of the vectorial sum operation [](#fig:vector-sum).

<div figure-id="fig:vector-sum" figure-caption="The sum of two vectors can be visualized with the parallelogram law.">
     <img src="placeholder.png" style='width: 15em'/>
</div>


#### Dot, or scalar, product {#vector-dot}

The dot, or scalar, product of two vectors ($\avec{u}$,$\avec{v} \in \mathbb{R}^3$) is a scalar ($a \in \mathbb{R}$) equal to the sum of the products of the components of the vectors. Equivalently, it can be expressed as the product of the magnitudes of the two vectors times the cosine of the angle between them, $\phi \in [0,2\pi)$.

\begin{definition}[Scalar product]\label{def:vector-dot-product}
\begin{align} \label{eq:vector-dot-product}
\avec{u} \cdot \avec{v} = u_1v_1+u_2v_2+u_3v_3 = \|u\|\|v\|\cos(\phi) \in \mathbb{R}
\end{align}
\end{definition}

The dot product is a measure of the _projection_ of vectors on one another ([](#fig:vector-dot-product)).

Note: When the two vectors are perpendicular, or orthogonal, the dot product is zero ($\cos(\pi/2) = 0$). This fact is often used as a test for orthogonality. Orthogonality is an important concept for linear spaces, as the most "efficient" basis are orthogonal.

<div figure-id="fig:vector-dot-product" figure-caption="The scalar product between two vectors measures the projection of one on each other.">
     <img src="placeholder.png" style='width: 30em'/>
</div>

<!-- It is useless to reference ####, as they have no section number. -->
#### Cross, or vector, product {#vector-cross}

While the dot product depends on the metric chosen in the space (the Euclidian norm, in our case), the cross product even requires the definition of an orientation, or handedness.

\begin{proposition}[Standard Basis]\label{prop:standard-basis}
In the Euclidian space $\mathbb{R}^3$, $\hat{\avec{i}}, \hat{\avec{j}}, \hat{\avec{k}}$ are the unit vectors for the standard basis, which is right handed.
\end{proposition}

In a right handed reference system such as the standard basis, the right hand rule ([](#fig:right-hand-rule)) is the handy-est way to identify the direction of the vector resulting from a cross product.

ProTip: There is a valid reason for which it is called the _right hand_ rule. Don't use your left hand because you are holding a pen with the right one.

<div figure-id="fig:right-hand-rule" figure-caption="The right hand rule points in the direction of the resulting vector from a cross product.">
     <img src="placeholder.png" style='width: 30em'/>
</div>

The cross, or vector, product between two vectors ($\avec{u}$, $\avec{v} \in \mathbb{R}^3$) is a vector that is orthogonal to each of the two vectors, hence is normal, or perpendicular, to the plane containing them. Its magnitude is given by the product of their magnitude times the sine of the angle between them, and its direction is indicated by the normal unit vector ($\hat{\avec{n}} \in \mathbb{R}^3$), identified by the right hand rule.

\begin{definition}[Vector product]\label{def:vector-cross-product}
\begin{align} \label{eq:vector-cross-product}
\avec{u} \times \avec{v} = [u_2v_3-u_3v_2, u_3v_1-u_1v_3, u_1v_2-u_2v_1]^T = \|u\|\|v\|\sin(\phi) \hat{\avec{n}}.
\end{align}
\end{definition}

\begin{remark}[Geometric interpretation]\label{rem:vec-cross-geom}
A cross product encodes two pieces on information: a direction, which is _orthogonal_ to the plane spanned by the two vectors, and a magnitude, which is equal to the area of the parallelogram having $\avec{u}$, and $\avec{v}$ as sides.
\end{remark}

Note: Keeping \eqref{eq:vector-cross-product} and [](#rem:vec-cross-geom) in mind, it should be intuitive to understand that:
\begin{align} \label{eq:vec-cross-vv-v0}
\avec{v} \times \avec{v} &= \avec{0}, \forall \avec{v} \in \mathbb{R}^n, \\
\avec{v} \times \avec{0} &= \avec{0}, \forall \avec{v} \in \mathbb{R}^n.
\end{align}

Note: The zero vector ($\avec{0}$) is a vector with zero magnitude, not the same as the number zero ($0$).

<!--
To obtain the components of $\avec{w}$ immagine the unit vectors $\hat{\avec{i}}, \hat{\avec{j}}, \hat{\avec{k}}$ as if they were placed on a wheel ([](#fig:wheel-trick)), in this order:

<div figure-id="fig:wheel-trick" figure-caption="The wheel trick.">
     <img src="placeholder.png" style='width: 30em'/>
</div>

Then each component of $\avec{w}$ is equal to:

\begin{align} \label{eq:vector-cross-product-components}
\avec{w} &= \avec{u} \times \avec{v} = (u_1)\hat{\avec{i}} +(u_2)\hat{\avec{j}} +(u_3)\hat{\avec{k}} \times (v_1)\hat{\avec{i}} +(v_2)\hat{\avec{j}} +(v_3)\hat{\avec{k}}\\
&= (u_2v_3-u_3v_2)\hat{\avec{i}} +(u_3v_1-u_1v_3)\hat{\avec{j}} +(u_1v_2-u_2v_1)\hat{\avec{k}}.
\end{align}
-->

Note: Each component of $\avec{w}$ is the difference of the products of the two _other_ components of $\avec{u}$, and $\avec{v}$, in the order given by the chosen handedness of the basis. This combination resembles a _cross_ ([](#fig:cross-product-explanation)), from which the name of _cross product_.

<div figure-id="fig:cross-product-explanation" figure-caption="Each component of the resulting vector is the product of the alternated other components, forming a cross.">
     <img src="placeholder.png" style='width: 30em'/>
</div>

Note: The components of a cross product can be computed through the Sarrus rule (see [](#matrix-determinant)).

As consequence of the vectorial product's definition and right handedness of the basis, the following hold true in the Cartesian space:

\begin{align} \label{eq:sb-cross-products}
\hat{\avec{i}} \times \hat{\avec{j}} &= \hat{\avec{k}} \\
\hat{\avec{j}} \times \hat{\avec{k}} &= \hat{\avec{i}} \\
\hat{\avec{k}} \times \hat{\avec{i}} &= \hat{\avec{j}}.
\end{align}


### Properties of vectors {#vector-properties}

In this section we highlight the properties of vector operations, that derive from their definitions.

#### Sum

The vector sum obejs the following:

- $\avec{u} + \avec{v} = \avec{v} + \avec{u}$,
- $(\avec{u} + \avec{v}) + \avec{w} = \avec{u} + (\avec{v} + \avec{w})$,
- $a(\avec{u} + \avec{v}) = a\avec{u} + a\avec{v}$,
- $(a+b)\avec{u} = a\avec{u} + b\avec{u}$,
- $\avec{u} + \avec{0} = \avec{u}$, therefore $\avec{u} + (-\avec{u}) = \avec{0}$.

#### Dot product

Letting $\phi \in [0,2\pi)$ be the angle between two vectors $\avec{u}, \avec{v}$, the dot product obejs the following:

- $\avec{u} \cdot \avec{v} = \| \avec{u} \|\| \avec{v} \|\cos(\phi)$,
- $\avec{u} \cdot \avec{u} = \| \avec{u} \|^2$,
- $\avec{u} \cdot \avec{v} = \avec{v} \cdot \avec{u}$,
- $\avec{u} \cdot (\avec{v} + \avec{w}) = \avec{u} \cdot \avec{v} + \avec{u} \cdot \avec{w}$,
- $a (\avec{u} \cdot \avec{v}) = (a\avec{u}) \cdot \avec{v}$,
- $\avec{0} \cdot \avec{u} = 0$
- $\avec{u} \cdot \avec{v}$ = 0 $\iff$ $\avec{u}=\avec{0}$, $\avec{v}=\avec{0}$, or $\avec{u} \bot \avec{v}$.

#### Cross product

Letting $\phi \in [0,2\pi)$ be the angle between two vectors $\avec{u}, \avec{v}$, the cross product obejs the following:

- $\avec{u} \times \avec{v} = \| \avec{u} \|\| \avec{v} \|\sin(\phi) \hat{\avec{n}}$,
- $\avec{u} \times \avec{v} = - \avec{v} \times \avec{u}$,
- $(a\avec{u}) \times \avec{v} = \avec{u} \times (a\avec{v}) = a(\avec{u} \times \avec{v})$,
- $\avec{u} \times (\avec{v} + \avec{w}) = \avec{u} \times \avec{v} + \avec{u} \times \avec{w}$,
- $\avec{u} \cdot (\avec{v} \times \avec{w}) = (\avec{u} \times \avec{v}) \cdot \avec{w}$,
- $\avec{u} \times (\avec{v} + \avec{w}) = (\avec{w} \cdot \avec{u}) \avec{v} - (\avec{v} \cdot \avec{u}) \avec{w} \neq (\avec{u} \times \avec{v}) + \avec{w}$,
- $\avec{u} \times \avec{v} = 0 \iff \avec{u}=\avec{0}, \avec{v}=\avec{0}$, or $\avec{u} \parallel \avec{v}$.


## Linear dependance {#linear-dep}

\begin{definition}[Linear dependance] \label{def:lin-dep}
Two or more vectors $\{\avec{v_1},\cdots,\avec{v_n}\}$ are _linearly dependant_ if there exists a set of scalars $\{a_1, \cdots, a_k\}, k \leq n$, that are _not all zero_, such that:
\[ \label{eq:lin-dep}
a_1\avec{v_1} + \cdots + a_k\avec{v_k} = \avec{0}.
\]
\end{definition}

Note: When \eqref{eq:lin-dep} is true, it is possible to write at least one vector as a linear combination of the others.

\begin{definition}[Linear independance] \label{def:lin-indep}
Two or more vectors ${\avec{v_1},\cdots,\avec{v_n}}$ are _linearly independant_ if \eqref{eq:lin-dep} can be satisfied only by $k=n$ and $a_i =0, \forall i = 1, \cdots, n$.
\end{definition}
<!--
\begin{definition}[Reference signals]\label{def:def-label}
A reference signal $\tilde{y}_t \in \mathcal{L}_2(\mathcal{T})$ is ...
\end{definition}

[](#def-label) is very important.

<div class="check" markdown="1">

Insert 'random' checks to keep the reader's attention up:

if you can't be woken up in the middle of the night and rememeber the definition of $\mathcal{L}_2(\cdot)$, read: [](#bib:placeholder)

</div>

\begin{definition}[Another definition]\label{def:another-def-label}
Lorem
\end{definition}
-->


<!--

<div class="example-usage" markdown="1">

This is a 'think about it' interrupt, used as attention grabber:

When a Duckiebot 'overshoots', it means that [...] and the following will happen [...].

</div>

### Section N: title-N (e.g.: Saving the world with PID)

And finally, this is how you save the world, in theory.

-->

## Pointers to Exercises {#theory-chapter-template-exercises-pointers}

Here we just add references to the suggested exercises, defined in the appropriate [exercise chapters](#part:exercises).

TODO: add exercises

## Conclusions

In this section we have defined the fundamental concept of linearity and linear dependance. Moreover, we have introduced vectors, with their operations and algebraic properties.

Vectors and linearity are the base for understanding linear spaces, which are useful because they introduce some fundamental concepts related to the foundation of _modeling_ of natural phenomena. Modeling will be invaluable in understanding the behavior of systems, and a powerful tool to _predict_ future behaviors of the system, and _control_ them when needed.

<!--
We have found that matrices are a very convenient way to represent linear spaces, and that the properties of the matrices such as eigenvalues and eigenvectors have important implications in characterizing these spaces.

These tools are useful because they are at the foundation of _modeling_ of natural phenomena. Modeling will be invaluable in understanding the behavior of systems, and a powerful tool to _predict_ future behaviors of the system, and _control_ them when needed.

We have learned that ... -->
<!--
- What did we do? (recap)
- What did we find? (analysis)
- Why is it useful? (synthesis)
- Final Conclusions (what have we learned)
-->
<!--
## Next Steps

- linearization of nonlinear equations
- state space representations
- basic kinematics
- basic dynamics -->


<!--
Strong of this new knowledge (what have we learned), we can now [...].
-->
<!--(Dear Santa, I would like class='additional-reading' here) -->
<div class="requirements" markdown="1">
<!--
Further Reading: insert here reference resources for the interested reader:
-->

See also: [](#bib:Savov2017)

See also: [Matrix cookbook](#bib:matrix-cookbook)

</div>


Author: Jacopo

Maintainer: Jacopo

Point of Contact: Jacopo


<!--
More academic examples

#### T-Example 1

Immagine a spring-mass-damper system...

#### T-Example M

[...]
-->

<!--
More Duckiebot related examples

#### I-Example 1


#### I-Example M

[...]
-->
