# \*Compiling the PDF version  {#duckuments-pdf status=ready}

This part describes how to compile the PDF version.

Note: The dependencies below are harder to install. If you don't manage
to do it, then you only lose the ability to compile the PDF. You can do `make compile`
to compile the HTML version, but you cannot do `make compile-pdf`.

## Installing `nodejs`

Ensure the latest version (>6) of `nodejs` is installed.

Run:

    $ nodejs --version
    6.xx

If the version is 4 or less, remove `nodejs`:

    $ sudo apt remove nodejs

Install `nodejs` using [the instructions at this page][nodejs].

[nodejs]: https://nodejs.org/en/download/package-manager/#debian-and-ubuntu-based-linux-distributions

<!-- $ sudo apt install node-less -->

Next, install the necessary Javascript libraries using `npm`:

    $ cd $DUCKUMENTS
    $ npm install MathJax-node jsdom@9.3 less



### Troubleshooting `nodejs` installation problems

The only pain point  in the installation procedure has been the installation of `nodejs` packages using `npm`. For some reason, they cannot be installed globally (`npm install -g`).

Do **not** use `sudo` for installation. It will cause problems.

If you use `sudo`, you probably have to delete a bunch of directories,
such as: `~/duckuments/node_modules`, `~/.npm`, and `~/.node_modules`, if they exist.

## Installing Prince

Install PrinceXML from [this page](https://www.princexml.com/download/).

## Installing fonts
<!--
Download STIX fonts from [this site][stix].

[stix]: https://sourceforge.net/projects/stixfonts/files/latest/download

Unzip and copy the ttf to `~/.fonts`:

    $ cp -R STIXv2.0.0 ~/.fonts -->

Copy the `~/duckuments/fonts` directory in `~/.fonts`:

    $ mkdir -p ~/.fonts    # create if not exists
    $ cp -R ~/duckuments/fonts ~/.fonts

and then rebuild the font cache using:

    $ fc-cache -fv


## Compiling the PDF

To compile the PDF, use:

    $ make compile-pdf

This creates the file:

    ./duckuments-dist/master/duckiebook.pdf
