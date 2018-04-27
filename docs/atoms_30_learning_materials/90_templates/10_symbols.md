# Symbols and conventions {#symbols-and-conventions status=ready}

Assigned: Andrea

## Conventions

You should not have to use presentation macros like `\mathcal`, `\boldsymbol`, etc.;
rather, for each class of things that we have (set, matrices, random variables, etc.)
we are going to define a LaTeX macro.

### Sets

Use the macro `\aset{X}` to refer to the set $\aset{X}$.

### Matrices

Use the macro `\amat{M}` to refer to the matrix $\amat{M}$.

### Tuples

To indicate tuples, use the macro `\tup`, which produces $\tup{a,b,c}$.

### Time series

If $x$ is a function of time, use $x_t$ rather than $x(t)$.

Bad: Consider the function $x(t)$.

Better: Consider the function $x_t$.

To refer to the time variable, use `\Time`: $t \in \Time$.

### Random variables

To refer to a random variable, use the macro `\rv`.
This is rendered using a **bold** symbol.

\begin{example}
$p(\rv{x}=x_0)$ is the probability that the random variable
$\rv{x}$ has the value $x_0 \in \aset{X}$.
\end{example}

### Well-known sets

Use `\reals` for the real numbers.

Use `\nats` for the natural numbers.

Use `\ints` for the integers numbers.


<col3 figure-id='tab:symbols' figure-caption="Basic symbols" class='symbols labels-row1'>
  <s>command</s>
  <s>result</s>
  <s></s>

  <code>\aset{X}, \aset{Y}</code>
  <s>$\aset{X}, \aset{Y}$</s>
  <s>Symbols for sets</s>

  <code>\amat{M}, \amat{P}</code>
  <s>$\amat{M}, \amat{P}$</s>
  <s>Symbols for matrices</s>

  <code>\avec{u}, \avec{v}</code>
  <s>$\avec{u}, \avec{v}$</s>
  <s>Symbols for vectors</s>

  <code>\nats</code>
  <s>$\nats$</s>
  <s>Natural numbers</s>

  <code>\ints</code>
  <s>$\ints$</s>
  <s>Integers</s>

  <code>\reals</code>
  <s>$\reals$</s>
  <s>Real numbers</s>

  <code>\definedas</code>
  <s>$\definedas$</s>
  <s> Defined as </s>


    <code>\tup{a,b,c}</code>
    <s>$\tup{a,b,c}$</s>
    <s> Tuples </s>


    <code>\Time</code>
    <s>$\Time$</s>
    <s> Time axis </s>

</col3>


## Spaces

Here are some useful symbols to refer to geometric spaces.

<col3 figure-id='tab:spaces' figure-caption="Spaces" class='symbols labels-row1'>
    <s>command</s>
    <s>result</s>
    <s></s>

    <code>\SOthree</code>
    <s>$\SOthree$</s>
    <s>Rotation matrices</s>


    <code>\SEthree</code>
    <s>$\SEthree$</s>
    <s>Euclidean group</s>

    <code>\SEtwo</code>
    <s>$\SEtwo$</s>
    <s>Euclidean group</s>

    <code>\setwo</code>
    <s>$\setwo$</s>
    <s>Euclidean group algebra</s>
</col3>

States and poses:

<col3 figure-id='tab:states' figure-caption="Poses and states" class='symbols labels-row1'>
    <s>command</s>
    <s>result</s>
    <s></s>

    <code>\pose</code>
    <s>$\pose_t \in \SEtwo$</s>
    <s>Pose of the robot in the plane</s>

    <s><code>\state_t \in \statesp</code></s>
    <s>$\state_t \in \statesp$</s>
    <s>System state (includes the pose, and everything else)</s>
</col3>


<style>
.symbols {
    font-size: smaller;
}
.symbols td {
    text-align: left;
}
</style>
