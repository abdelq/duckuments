# Convex optimization {#preliminaries-convex-optimization status=beta}

Convex optimization is a minimization technique where one optimizes a convex function over convex sets.  
In the following few lines we'll talk about the standard form of convex optimization.  

## Motivation
Often there are problems which should be minimized but with respect to some constraint.
One can think of a nutrition problem where people want to spend the least amount of money possible on food while still having all the important levels of nutrition. So one would minimize the cost with respect to inequality constraints like the amount of calcium has to be bigger than 1000 milligrams per day or the amount of vitamin C has to be bigger than 90 milligrams a day.

[ [source] ](https://jeremykun.com/2014/06/02/linear-programming-and-the-most-affordable-healthy-diet-part-1/)

## Mathematical description of the problem
Mathematically speaking the problem would be formulated as follows.
One defines the function $f(x)$ to be minimized. Now a point $x^*$ has to be found such that $f(x^* )=\text{min}{f(x): x \in X}$ which means $f(x^* )$ is the minimal function value of all values $x$ in some feasible set $X$.  
The function $f(x)$ can be minimized now subject to several constraints.  
There are basically two possibilities:
1. inequality constraints $h(x) \leq 0$ or $h(x) \geq 0$
2. equality constraints $h(x) = 0$ which can be replaces by a pair of inequality constraints $h(x) \leq 0$ and $-h(x) \leq 0$
The standard form would be formulated as follows:
\[ \text{minimize}_{x } f(x)\]
\[\text{subject to } g_i(x) \leq 0, i = 1, ..., m\]
\[ \text{and } h_i(x) = 0, i = 1, ..., p \]


## Limits
The functions $f(x)$ and $g_i(x)$ have to be convex and $h_i(x)$ has to be affine such that the replacement of the equality constraint by two inequality constraints is valid.
