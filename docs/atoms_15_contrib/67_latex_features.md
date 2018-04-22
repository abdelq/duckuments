# Using LaTeX constructs in documentation {#using-latex status=ready}

<div class='requirements' markdown="1">

Requires: Working knowledge of LaTeX.

</div>

## Embedded LaTeX

You can use $\LaTeX$ math, environment, and references. For example, take a look at

\[
    x^2 = \int_0^t f(\tau)\ \text{d}\tau
\]

or refer to [](#prop:example).

\begin{proposition}[Proposition example]\label{prop:example}
This is an example proposition: $2x = x + x$.
\end{proposition}

The above was written as in [](#code:latex-code).

<pre figure-id="code:latex-code" figure-caption='Use of LaTeX code.'>
<code>
You can use &#36;\LaTeX&#36; math, environment, and references.
For example, take a look at

&#92;[
    x^2 = \int_0^t f(\tau)\ \text{d}\tau
&#92;]

or refer to [](#prop:example).

&#92;begin{proposition}[Proposition example]&#92;label{prop:example}
This is an example proposition: &#36;2x = x + x&#36;.
&#92;end{proposition}
</code>
</pre>

For the LaTeX environments to work properly you *must* add a `\label`
declaration inside. Moreover, the label must have a prefix that is adequate
to the environment. For example, for a proposition, you must insert `\label{prop:![name]}`
inside.

The following table shows the list of the LaTeX environments supported
and the label prefix that they need.

<col2 figure-id="tab:environments" figure-caption="LaTeX environments and label prefixes">
    <code>definition</code>
    <code>def:![name]</code>
    <code>proposition</code>
    <code>prop:![name]</code>
    <code>remark</code>
    <code>rem:![name]</code>
    <code>problem</code>
    <code>prob:![name]</code>
    <code>theorem</code>
    <code>thm:![name]</code>
    <code>lemma</code>
    <code>lem:![name]</code>
</col2>


Examples of all environments follow.

<div class='example-usage' markdown="1">

  <pre><code>&#92;begin{definition}   \label{def:lorem}
Lorem
&#92;end{definition}</code></pre>

\begin{definition}\label{def:lorem}Lorem\end{definition}

  <pre><code>&#92;begin{proposition}   \label{prop:lorem}
Lorem
&#92;end{proposition}</code></pre>

\begin{proposition}\label{prop:lorem}Lorem\end{proposition}

  <pre><code>&#92;begin{remark}   \label{rem:lorem}
Lorem
&#92;end{remark}</code></pre>

\begin{remark}\label{rem:lorem}Lorem\end{remark}

  <pre><code>&#92;begin{problem}    &#92;label{prob:lorem}
Lorem
&#92;end{problem}</code></pre>

\begin{problem}\label{prob:lorem}Lorem\end{problem}

  <pre><code>&#92;begin{example}   \label{exa:lorem}
Lorem
&#92;end{example}</code></pre>

\begin{example}\label{exa:lorem}Lorem\end{example}

  <pre><code>&#92;begin{theorem}   \label{thm:lorem}
Lorem
&#92;end{theorem}</code></pre>

\begin{theorem}\label{thm:lorem}Lorem\end{theorem}

  <pre><code>&#92;begin{lemma}   \label{lem:lorem}
Lorem
&#92;end{lemma}</code></pre>

\begin{lemma}\label{lem:lorem}Lorem\end{lemma}

    I can also refer to all of them:
    [](#def:lorem),
    [](#prop:lorem),
    [](#rem:lorem),
    [](#prob:lorem),
    [](#exa:lorem),
    [](#thm:lorem),
    [](#lem:lorem).

I can also refer to all of them:
[](#def:lorem),
[](#prop:lorem),
[](#rem:lorem),
[](#prob:lorem),
[](#exa:lorem),
[](#thm:lorem),
[](#lem:lorem).

</div>

## LaTeX equations {#latex-equations}

We can refer to equations, such as \eqref{eq:one}:

\begin{equation}
    2a = a + a  \label{eq:one}
\end{equation}

This uses `align` and contains  \eqref{eq:two} and \eqref{eq:three}.

\begin{align}
    a &= b \label{eq:two} \\
      &= c \label{eq:three}
\end{align}

<pre trim="1">
<code trim="1">
We can refer to equations, such as \eqref{eq:one}:

\<span/>begin{equation}
    2a = a + a          &#92;label{eq:one}
\<span/>end{equation}

This uses `align` and contains  \eqref{eq:two} and \eqref{eq:three}.

\<span/>begin{align}
    a &amp;= b       &#92;label{eq:two} \\
      &amp;= c       &#92;label{eq:three}
\<span/>end{align}
</code>
</pre>

Note that referring to the equations is done using the syntax `\eqref{eq:![name]}`,
rather than `[](#eq:![name])`.


## LaTeX symbols

The LaTeX symbols definitions are in a file called [`docs/symbols.tex`][symbols].


[symbols]: github:org=Duckietown,repo=duckuments,path=docs/symbols.tex


Put all definitions there; if they are centralized it is easier to check
that they are coherent.


## Bibliography support {#bibliography-support}

You need to have installed `bibtex2html`.

The system supports Bibtex files.

Place `*.bib` files anywhere in the directory.

Then you can refer to them using the syntax:

    [](#bib:![bibtex ID])

For example:

    Please see [](#bib:siciliano07handbook).

Will result in:

> Please see [](#bib:siciliano07handbook).

## Embedding Latex in Figures through SVG {#svg-figures}

<div class='requirements' markdown="1">

Requires: In order to compile the figures into PDFs you need to have Inkscape installed. Instructions to download and install Inkscape are [here](https://inkscape.org/en/release/0.92.2/).

</div>


To embed latex in your figures, you can add it directly to a file and save it as `![filename].svg` file and save anywhere in the `/docs` directory.

You can run:

    $ make process-svg-figs

And the SVG file will be compiled into a PDF figure with the LaTeX commands properly interpreted.

You can then include the PDF file in a normal way ([](#figures)) using `![filename].pdf` as the filename in the <code>&lt;img&gt;</code> tag.


<div figure-id="fig:inkscape">
    <figcaption>Embedding LaTeX in images</figcaption>

    <div figure-id="subfig:1">
        <figcaption>Image saved as svg</figcaption>
          <img src="sample-no-process.converted.png" style='width: 20em'/>
    </div>
    <div figure-id="subfig:2">
        <figcaption>Image as PDF after processing</figcaption>
          <img src="sample.pdf" style='width: 20em; height: auto'/>
    </div>
</div>



It can take a bit of work to get the positioning of the code to appear properly on the figure.
