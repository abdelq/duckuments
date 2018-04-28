# Git LFS {#git-lfs status=ready}

This describes Git LFS.

## Generic installation instructions {#git-lfs-install}

See instructions at:

> [https://git-lfs.github.com/](https://git-lfs.github.com/)

## Ubuntu 16 installation (laptop)

Following [these instructions](https://github.com/git-lfs/git-lfs/wiki/Installation),
run the following:

    $ sudo add-apt-repository ppa:git-core/ppa
    $ curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
    $ sudo apt update
    $ sudo apt install git-lfs

<!-- $ git lfs install -->

## Raspberry Pi 3 {status=draft}

Note: unresolved issues.

The instructions above do not work.

Following [this](https://bioinfoexpert.com/2016/08/25/installation-of-git-lfs-on-ubuntu-rpi2-armf/), the error
that appears is that golang on the Pi is 1.6 instead it should be 1.7.

## Troubleshooting {#lfs-troubleshooting}

Symptom: The binary files are not downloaded. In their place, there
are short "pointer" files.

If you have installed LFS after pulling the repository and you see
only the pointer files, do:

    $ git lfs pull --all
