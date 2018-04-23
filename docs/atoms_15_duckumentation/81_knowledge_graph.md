# Knowledge graph {#knowledge-graph lang=en status=draft type=text}

Note: This chapter describes something that is not implemented yet.

## Formalization

### Atoms

\begin{definition}[Atom]\label{def:an-atom}
An *atom* is a concrete resource (text, video) that is the smallest
unit that is individually addressable. It is indivisible.
\end{definition}

Each atom as a type, as follows:

<!--
Examples of atoms include:


    - `theory`;
    - `setup`: setup instructions;
    - `demo`: demo instructions;
    - `exercise`: exercises;
    - `slides`: lecture slides;
    - `video`: lecture videos, instruction videos.
    - `reference`: manuals about specific software; "how to solder".
-->

    text
      text/theory
      text/setup
      text/demo
      text/exercise
      text/reference
      text/instructor-guide
      text/quiz
    video
      video/lecture
      video/instructable
      video/screencast
      video/demo



<!--
slides

Resources:
    markdown
    pdf
    image jpg


  "An atom is made up of resources (markdown source, images, other attachments, etc.), but these resources are not indexable by themselves. They are always presented as part of an atom."
-->

### Semantic graph of atoms {#atoms-graphs}

Atoms form a directed graph, called "semantic graph".

Each node is an atom.

The graph has four different types of edges:

* "**Requires**" edges describe a strong dependency: "You need to have done this. Otherwise it will not work."
* "**Recommended**" edges describe a weaker dependency; it is not strictly necessary to have done that other thing, but it will significantly improve the result of this.
* "**Reference**" edges describe background information. "If you don't know / don't remember, you might want to see this"
* "**See also**" edges describe interesting materials for the interested reader. Completely optional; it will not impact the result of the current procedure.

### Modules

A "module" is an abstraction from the point of view of the teacher.

\begin{definition}[Module]\label{def:module}
A *module* is a directed graph, where the nodes are either atoms or other modules,
and the edges can be of the four types described in [](#atoms-graphs).
\end{definition}

Because modules can contain other modules, they allow to describe hierarchical
contents. For example, a class module is a module that contains other modules;
a "degree" is a module that contains "class" modules, etc.

Modules can overlap. For example, a "Basic Object Detection"
and an "Advanced Object Detection" module might have a few atoms in common.

## Atoms properties

Each atom has the following **properties**:

- An **ID** (alphanumeric + `-` and '_'). The ID is used for cross-referencing.
  It is the same in all languages.
- A **type**, as above.

There might be different **versions** of each atom. This is used primarily
for dealing with translations of texts, different representations of the same image,
Powerpoint vs Keynote, etc.

A version is a tuple of attributes.

The attributes are:

- **Language**: A [language code][codes], such as `en-US` (default), `zh-CN`, etc.

- **Mime type**: a MIME type.

[codes]: https://en.wikipedia.org/wiki/Language_localisation


Each atom version has:


- A human-readable **title**.
- A human-readable **summary** (1 short paragraph).


### Status values (updated Sep 12) {#status-values status=recently-updated }

Each document has a **status** value.

The allowed values are described in [](#tab:status).

<col2 figure-id="tab:status">
    <figcaption>Status codes</figcaption>
    <code>draft</code> <s>We just started working on it, and it is not ready
                      for public consumption.</s>
    <code>beta</code>  <s>Early reviewers should look at it now.</s>
    <code>ready</code> <s>The document is ready for everybody.</s>
    <code>recently-updated</code> <s> The document has been recently updated (less than 1 week)</s>
    <code>to-update</code> <s>A new pass is needed on this document, because
    it is not up to date anymore.</s>
    <code>deprecated</code> <s>The document is ready for everybody.</s>
</col2>


## Markdown format for text-like atoms {#markdown-header}

For the text-like resources, they are described in Markdown files.

The name of the file does not matter.

All files are encoded in UTF-8.

Each file starts with a `H1` header. The contents is the title.

The header has the following attributes:

1. The ID. (`{#ID}`)
2. The status is given by an attribute `status`, which should be value of the values in [](#tab:status).
2. (Optional) The language is given by an attribute `lang` (`{lang=en-US}`).
3. (Optional) The type is given by an attribute `type` (`{type=demo}`).

Here is an example of a header with all the attributes:

<div figure-id="code:calib-en" markdown="1">
 <figcaption>`calibration.en.md`</figcaption>

``` .markdown
# Odometry calibration {#odometry-calibration lang=en-US type='text/theory' status=ready}

This first paragraph will be used as the "summary" for this text.

```

</div>

And this is how the Italian translation would look like:


<div figure-id="code:calib-it" markdown="1">
 <figcaption>`calibration.it.md`</figcaption>

``` .markdown
# Calibrazione dell'odometria {#odometry-calibration lang=it type='text/theory' status=draft}

Questo paragrafo sarà usato come un sommario del testo.

```

</div>




<!--
<col4 figure-id='tab:atoms-types'>
    <s>Type of atom</s>
    <s>Format</s>
    <s>Where</s>
    <s>Conventions</s>

    <s>Text</s>
    <s>Markdown</s>
    <s>duckuments</s>
    <s><code># Title {#ID type=text lang=en status=draft}</code></s>

    <s>Setup instructions</s>
    <s>Markdown</s>
    <s>duckuments</s>
    <s><code># Title {#ID type=setup lang=en status=draft}</code></s>

    <s>Demo instructions</s>
    <s>Markdown</s>
    <s>duckuments</s>
    <s><code># Title {#ID type=demo lang=en status=draft}</code></s>

    <s>Exercises</s>
    <s>Markdown</s>
    <s>duckuments</s>
    <s><code># Title {#ID type=exercise lang=en status=draft}</code></s>

    <s>Reference</s>
    <s>Markdown</s>
    <s>duckuments</s>
    <s><code># Title {#ID type=reference lang=en status=draft}</code></s>

</col4> -->

<!--
    <s>Images</s>
    <s>SVG, PDF, JPG</s>
    <s>duckuments</s>
    <s>The filename is <code>ID.{png,jpg,pdf}</code></s>


</col2> -->

<!--
IPTC
$ exiftool magician_chassis.jpg  "-Title='The Magician chassis'"
http://www.iptc.org/std/photometadata/specification/IPTC-PhotoMetadata-201007.pdf -->


## How to describe the semantic graphs of atoms

In the text, you describe the semantic graph using tags and IDs.

In Markdown, you can give IDs to sections using the syntax:

    # Setup step 1  {#setup-step1}

    This is the first setup step.

Then, when you write the second step, you can add a
a semantic edge using the following.

    # Setup step 2  {#setup-step2}

    This is the second setup step.

    Requires: You have completed the first step in [](#setup-step1).

The following table describes the syntax for the different types
of semantic links:

<col2 figure-id='tab:links' figure-caption="Semantic links">
    <s>Requires</s>
    <s><pre><code>Requires: You need to have done []<span></span>(#setup-step).</code></pre></s>

    <s>Recommended</s>
    <s><pre><code>Recommended: It is better if you have setup Wifi as in []<span></span>(#setup-wifi).</code></pre></s>

    <s>Reference</s>
    <s><pre><code>Reference: For more information about <code>rostopic</code>, see []<span></span>(#rostopic).</code></pre></s>

    <s>See also</s>
    <s><pre><code>See also: If you are interested in feature detection, you might want to learn about [SIFT](#SIFT).</code></pre></s>
</col2>

<style>
#tab\:links {
    font-size: smaller;
}
#tab\:links code {
    font-size: 80%;
}
#tab\:links td:first-child {
    display:block;
    width: 10em;
}
#tab\:links td {
    text-align: left;
    padding-bottom: 0.5em;
}
</style>

## How to describe modules

TODO: Define a micro-format for this.


<!--
### Example

Here is

    module:calibration:
        includes:
            lecture:basic-kinematics
            text:basic-kinematics
            lecture:
            video:calibration_of_robots
        edges:



    module:calibration-advanced:

             -->
