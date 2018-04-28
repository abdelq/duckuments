# Sets {#sets status=draft}

Assigned: Dzenan

<div class='requirements' markdown='1'>

Result: k:sets

</div>

## Definition

\begin{definition}[Set]\label{def:set}
A set $\aset{X} = \{x_1, x_2, \dots\}$ is a well-defined collection of distinct _elements_, or _members_ of the set, $x_i$, $i = 1, 2, \dots$.
\end{definition}


## Maps {#maps}

<div class='requirements' markdown='1'>

Requires: k:sets

Result: k:maps

</div>

## Definition

We define a _function_ (or _map_) as a mapping between _sets_.

\begin{definition}[Function]\label{def:function}
A function $f : \aset{X} \to \aset{Y}$ is a mapping between the sets $\aset{X}$ and $\aset{Y}$. For every input element $x \in \aset{X}$, the mapping will associate an output $y = f(x) \in \aset{Y}$.
\end{definition}

## Properties of maps

Maps can be classified by the nature of the relationship between inputs and outputs in: _injective_, _surjective_ or _bijective_ [add-ref]().


### Injective maps

TODO: to write

### Surjective maps

TODO: to write

### Bijective maps

TODO: to write


# Numbers {#numbers status=draft}

<div class='requirements' markdown='1'>

Requires: k:sets

Result: k:naturals, k:integers, k:reals

</div>

## Natural numbers {#intro-nats status=beta}

$\nats = \{0, 1, 2, \cdots\}$

The natural numbers are the set positive numbers, including zero.

Given two natural their addition is always a natural number:

\[ a+b = c \in \nats, \forall a,b \in \nats. \label{eq:intro-nats}\]

The same does not hold of the subtraction operation:

\[ a-b = c \in \nats \iff a \geq b.
\]

For this reason set of integer numbers is defined.

## Integers

$\ints = \{\cdots, -2, -1, 0, 1, 2, \cdots \}$

The integers are the set of positive and negative natural numbers, including the zero. By definition, the set of integers includes the naturals: $\ints \subset \nats$.

The sum (i.e., addition and subtraction) of two integers is always an integer:
\begin{align}
a + b &= c \in \ints, \forall a,b \in \nats \\
a - b &= c \in \ints, \forall a,b \in \nats.
\end{align}

The multiplication of two integers is always an integer, but the same does not apply for the division operation:

\[
\frac{a}{b} = c \in \ints \iff a = kb, k \in \ints, b \neq 0.
\]

For this reason the rational numbers are introduced.

## Rationals

The set of rational numbers includes all fractions of integers: $\rats = \{ c | \frac{a}{b} = c, a,b \in \ints, b \neq 0 \}$.

The set of rational number is complete under sum and product (i.e., multiplication and division), but not under other operations such as the root. E.g., $\sqrt{2}$ cannot be expressed as a fraction of two integers. These numbers are not rational, and therefore are defined as irrationals.

## Irrationals

Irrational numbers are all those numbers that cannot be expressed as a fraction. Notable examples of irrational numbers include the aforementioned $\sqrt{2}$, but even pi ($\pi$) and the Euler number ($e$).

Irrational numbers are not typically referred to as as a set by themselves, rather, the union of the rational and irrational numbers defines the set of _reals_.

## Reals

The real numbers ($\reals$) are arguably the most used set of numbers, and are often considered the default set if no specification is provided.

The real numbers are defined as the union of rational and irrational numbers, and therefore by definition include the integers and the naturals.

The reals are still not complete under all "canonical" operations. In fact, there is no solution to the root (of even index) of a negative number.

For this reason, the complex numbers are introduced.  

## Complex

Complex numbers are defined as the sum of a real and an imaginary part:

\[ z = a + ib, a,b \in \reals, i = \sqrt{-1}
\]

and can be represented on the plane of Gauss, a Cartesian plane featuring the real part of $z$, $Re(z) = a$, on the x-axis and the imaginary part, $Im(z)=b$, on the y-axis ([](#fig:gauss-plane)).

<div figure-id="fig:gauss-plane" figure-caption="The Gaussian plane is used to represent complex numbers">
     <img src="placeholder.png" style='width: 15em'/>
</div>

Complex numbers introduce the concept of _phase_ of a number, which is related to its "orientation", and are invaluable for describing many natural phenomena such as electricity and applications such as signal decoders.

For more information on the algebra and properties of natural numbers:

see: [](#intro-algebra-complex).
