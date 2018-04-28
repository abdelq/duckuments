# Contributing to the documentation {#part:contribute-to-docs status=ready}

# Introduction {status=ready}

## Where the documentation is

All the documentation is in the repository `duckietown/duckuments`.

The documentation is written as a series of small files in Markdown format.

It is then processed by a series of scripts to create this output:

* a publication-quality PDF;
* an online HTML version;

You can find all these artifacts produced at the site [`docs.duckietown.org`](http://docs.duckietown.org).


## Editing links

The simplest way to contribute to the documentation is to click any of the "✎" icons next to the headers.

They link to the "edit" page in Github. There, one can make and commit the edits in only a few seconds.


# Installing the documentation system {#installing-docs-system status=ready}

In the following, we are going to assume that the documentation system is installed in `~/duckuments`. However, it can be installed anywhere.

We are also going to assume that you have setup a Github account with working public keys.

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

Here, note we are using `git lfs clone` -- it's much faster, because it downloads the Git LFS files in parallel.

If it fails, it means that you do not have Git LFS installed. See [](#git-lfs).

The command `--depth 100` tells it we don't care about the whole history.


### Setup the virtual environment

Use this to install a virtual environment and dependencies:

    $ cd ~/duckuments
    $ make install    

TODO: In other distributions you might need to use `venv` instead of `virtualenv`.


## Compiling the documentation   {#compiling-master}

To compile all the books, run:

    $ make clean all 

To see the result, open the file

    ./duckuments-dist/index.html

If you want to do incremental compilation, you can omit the `clean` and just
use:

    $ make all
    
## Compiling a single book

After you have compiled all the books, 
you can use one of the following commands to re-compile one single book:

    $ make duckumentation
    $ make the_duckietown_project 
    $ make opmanual_duckiebot_base 
    $ make opmanual_duckiebot_fancy 
    $ make opmanual_duckietown 
    $ make software_carpentry 
    $ make software_devel 
    $ make software_architecture 
    $ make class_fall2017 
    $ make class_fall2017_projects 
    $ make learning_materials 
    $ make exercises 
    $ make drafts 
    $ make guide_for_instructors 
    $ make deprecated 
    $ make preliminaries

If compilation is unsuccesfull, try:

    $ make clean


## The workflow to edit documentation  {#workflow status=deprecated}

TODO: write update workflow

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

If you say something like "This happens for Figure 3", then it is hard to know which figure you are referencing exactly, because numbering changes from commit to commit.

If you want to refer to specific parts of the text, please commit all your work on your branch, and obtain the name of the commit using the following commands:

    $ git -C ~/duckuments rev-parse HEAD      # commit for duckuments
    $ git -C ~/duckuments/mcdp rev-parse HEAD # commit for mcdp
 
