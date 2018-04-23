# Contributing to the documentation {#contribute-to-docs status=ready}

## Where the documentation is

All the documentation is in the repository `duckietown/duckuments`.

The documentation is written as a series of small files in Markdown format.

It is then processed by a series of scripts to create this output:

* [a publication-quality PDF][master-pdf];
* [an online HTML version, split in multiple pages][master-split];
* [a one-page version][master-html].

[master-pdf]: http://book.duckietown.org/master/duckiebook.pdf
[master-html]: http://book.duckietown.org/master/duckiebook.html
[master-split]: http://book.duckietown.org/master/duckiebook/index.html
<!-- * [HTML (single-page)][master-html]; -->

## Editing links

The simplest way to contribute to the documentation is to click any of the "✎" icons next to the headers.

They link to the "edit" page in Github. There, one can make and commit the edits in only a few seconds.


## Installing the documentation system {#installing-docs-system}

In the following, we are going to assume that the documentation system is
installed in `~/duckuments`. However, it can be installed anywhere.

We are also going to assume that you have setup
a Github account with working public keys.

See: [Basic SSH config](#ssh-local-configuration).

See: [Key pair creation](#howto-create-key-pair).
 
See: [Adding public key on Github](#howto-add-pubkey-to-github).


We are also going to assume that you have installed the `duckietown/software` in `~/duckietown`.

### Dependencies (Ubuntu 16.04)

On Ubuntu 16.04, these are the dependencies to install:

    $ sudo apt install libxml2-dev libxslt1-dev
    $ sudo apt install libffi6 libffi-dev
    $ sudo apt install python-dev python-numpy python-matplotlib
    $ sudo apt install virtualenv
    $ sudo apt install bibtex2html pdftk
    $ sudo apt install imagemagick



### Download the `duckuments` repo

Download the `duckietown/duckuments` repository in the `~/duckuments` directory:

    $ git lfs clone --depth 100 git@github.com:duckietown/duckuments ~/duckuments

Here, note we are using `git lfs clone` -- it's much faster, because it downloads
the Git LFS files in parallel.

If it fails, it means that you do not have Git LFS installed. See [](#git-lfs).

The command `--depth 100` tells it we don't care about the whole history.


### Setup the virtual environment

Next, we will create a virtual environment using inside  the `~/duckuments`
directory. Make sure you are running Python 2.7.x. Python 3.x is not supported at the moment.

Change into that directory:

    $ cd ~/duckuments

Create the virtual environment using `virtualenv`:

    $ virtualenv --system-site-packages deploy

Other distributions: In other distributions you might need to use `venv` instead of `virtualenv`.

Activate the virtual environment:

    $ source ~/duckuments/deploy/bin/activate

### Setup the `mcdp` external repository

Make sure you are in the directory:

    $ cd ~/duckuments

Clone the `mcdp` external repository, with the branch `duckuments`.

    $ git clone -b duckuments git@github.com:AndreaCensi/mcdp

Install it and its dependencies:

    $ cd ~/duckuments/mcdp
    $ python setup.py develop

Note: If you get a permission error here, it means you have not properly
activated the virtual environment.

Other distributions: If you are not on Ubuntu 16, depending on your system, you might need to install these other dependencies:

    $ pip install numpy matplotlib

You also should run:

    $ pip install -U SystemCmd==2.0.0

## Compiling the documentation (updated Sep 12) {#compiling-master status=recently-updated }

<div class="check" markdown="1">

Make sure you have deployed and activated the virtual environment. You can check
this by checking which `python` is active:

    $ which python
    /home/![user]/duckuments/deploy/bin/python

</div>

<!--
Then:

    $ cd ~/duckuments
    $ mkdir duckuments-dist

 This creates the directory `duckuments-dist`, which contains
the "live" website published by Github using the "Github Pages" mechanism at the URL `book.duckietown.org`.

<div class="check" markdown="1">

At this point, please make sure that you have these two `.git` folders:

    ~/duckuments/.git
    ~/duckuments/duckuments-dist/.git

</div> -->

To compile the master versions of the docs, run:

    $ make master-clean master

To see the result, open the file

    ./duckuments-dist/master/duckiebook/index.html

If you want to do incremental compilation, you can omit the `clean` and just
use:

    $ make master

This will be faster. However, sometimes it might get confused. At that point,
do `make master-clean`.

### Compiling the Fall 2017 version only (introduced Sep 12) {#compiling-fall2017 status=recently-updated}

To compile the Fall 2017 versions of the docs, run:

    $ make fall2017-clean fall2017

To see the result, open the file

    ./duckuments-dist/master/duckiebook/index.html


For incremental compilation, use:

    $ make fall2017

### Single-file compilation {#compile-single-file}

There is also the option to compile one single file.

To do this, use:

    $ ./compile-single ![path to .md file]

This is the fastest way to see the results of the editing; however, there are limitations:

- no links to other sections will work.
- not all images might be found.


## The workflow to edit documentation (updated Sep 12) {#workflow status=recently-updated}

This is the basic workflow:

1. Create a branch called `![yourname]-branch` in the `duckuments` repository.
1. Edit the Markdown in the `![yourname]-branch` branch.
2. Run `make master` to make sure it compiles.
3. Commit the Markdown and push on the `![yourname]-branch`  branch.
4. Create a pull request.
5. Tag the group `duckietown/gardeners`.


See: Create a pull request from the command-line using [`hub`](#hub).

## Reporting problems

First, see the section <a href="#markduck-troubleshooting" class='name_number'></a> for
common problems and their resolution.

Please report problems with the duckuments using [the `duckuments` issue tracker][tracker].
If it is urgent, please tag people (Andrea); otherwise these are processed in batch mode every few days.

[tracker]: https://github.com/duckietown/duckuments/issues


If you have a problem with a generated PDF, please attach the offending PDF.

If you say something like "This happens for Figure 3", then it is hard
to know which figure you are referencing exactly, because numbering changes
from commit to commit.

If you want to refer to specific parts of the text, please commit all your work on your branch,
and obtain the name of the commit using the following commands:

    $ git -C ~/duckuments rev-parse HEAD      # commit for duckuments
    $ git -C ~/duckuments/mcdp rev-parse HEAD # commit for mcdp

<!--
JT: this is a test to show how to edit the docs
-->


<!-- don't need to do it manually.

To deploy the documentation, jump into the `DUCKUMENTS/duckuments-dist` directory.

Run the command `git branch`. If the out does not say that you are on the branch `gh-pages`,
then one of the steps before was done incorrectly.

    $ cd $DUCKUMENTS/duckuments-dist
    $ git branch
    ...
    * gh-pages
    ...

Now, after triple checking that you are in the `gh-pages` branch, you can
use `git status` to see the files that were added or modified,
and simply use `git add`, `git commit` and `git push` to push the files
to Github. -->
