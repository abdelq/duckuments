# Matrices basics {#matrix-definitions status=draft}

Assigned: Dzenan

<div class='requirements' markdown='1'>

Requires: k:basic_math

Requires: k:linear_algebra

Result: k:matrices

</div>

A matrix:

 \[
 \amat{A} = \left[  \begin{array}{ccc} a_{11}  & \dots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1}  & \dots & a_{mn} \end{array} \right] \in \reals^{m \times n} \label{eq:matrix}
 \]

 is a table ordered by ($m$) horizontal rows and ($n$) vertical columns. Its elements are typically denoted with lower case latin letters, with subscripts indicating their row and column respectively. For example, $a_{ij}$ is the element of $A$ at the $i$-th row and $j$-th column.

 <div figure-id="fig:matrix" markdown="1">
      <figcaption>A matrix. This image is taken from [](#bib:wiki-matrix)</figcaption>
      <img src="matrix.svg" style='width: 15em'/>
 </div>

 Note: A vector is a matrix with one column.

 <!--
 Before delving in the many and important meanings and interpretations of matrices, we will first introduce some terminology and notable matrices.
 -->

## Matrix dimensions {#mat-dim}

The number of rows and columns of a matrix are referred to as the matrix _dimensions_. $\amat{A} \in \reals^{m \times n}$ has dimensions $m$ and $n$.

\begin{definition}[Fat matrix] \label{def:mat-fat}
 When $n > m$, i.e., the matrix has more columns than rows, $\amat{A}$ is called _fat_ matrix.
\end{definition}

\begin{definition}[Tall matrix] \label{def:mat-tall}
When $n < m$, i.e., the matrix has more rows than columns, $\amat{A}$ is called _tall_ matrix.
\end{definition}

\begin{definition}[Fat matrix] \label{def:mat-square}
When $n = m$, $\amat{A}$ is called _square_ matrix.
\end{definition}

Note: Square matrices are particularly important.

## Matrix diagonals

- Main diagonal

- Secondary diagonal

## Diagonal matrix {#mat-diagonal}

\begin{definition}[Diagonal matrix] \label{def:mat-diagonal}
A diagonal matrix has non zero elements only on its main diagonal.
\begin{align}
\amat{A} = \left[  \begin{array}{ccc}
a_11   & 0        & \dots  & 0 \\
0      & a_22     & \ddots & \vdots \\
\vdots & \ddots   & \ddots & 0 \\
0      & \dots    & 0      & a_nn
\end{array} \right]
\end{align}
\end{definition}

## Identity matrix {#mat-identity}

\begin{definition}[Identity matrix] \label{def:mat-identity}
An identity matrix is a diagonal square matrix with all elements equal to one.
\begin{align}
\amat{I} = \left[  \begin{array}{ccc}
1   & 0        & \dots  & 0 \\
0      & 1     & \ddots & \vdots \\
\vdots & \ddots    & \ddots & 0 \\
0      & \dots    & 0      & 1
\end{array} \right]
\end{align}
\end{definition}

## Null matrix {#mat-null}

\begin{definition}[Null matrix] \label{def:mat-null}
The null, or Zero, matrix is a matrix whos elements are all zeros.
\begin{align}
\amat{0} = \left[  \begin{array}{ccc} 0  & \dots & 0 \\ \vdots & \ddots & \vdots \\ 0  & \dots & 0 \end{array} \right]
\end{align}
\end{definition}

## Determinant {#matrix-determinant}

- 2x2
- 3x3
- nxn

## Rank of a matrix {#intro-matrix-rank}

## Trace of a matrix {#intro-matrix-trace}
