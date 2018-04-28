# Source code control with Git {#git-reference status=ready}

Assigned: Andrea

## Background reading

See: [Good book](https://git-scm.com/book/en/v2)

See: [Git Flow](http://nvie.com/posts/a-successful-git-branching-model/)

## Installation

The basic Git program is installed using

    $ sudo apt install git

Additional utilities for `git` are installed using:

    $ sudo apt install git-extras

This include the `git-ignore` utility.


## Setting up global configurations for Git  {#howto-git-local-config}

This should be done twice, once on the laptop, and later, on the robot.

These options tell Git who you are:

    $ git config --global user.email "![email]"
    $ git config --global user.name  "![full name]"

Also do this, and it doesn't matter if you don't know what it is:

    $ git config --global push.default simple

## Git tips

### Delete branches


Delete local:

    $ git branch -d ![branch-name]

Delete remote:

    $ git push origin --delete ![branch-name]


Propagate on other machines by doing:

    $ git fetch --all --prune


### Shallow clone

You can clone without history with the command:

    $ git clone --depth 1 ![repository URL]

## Git troubleshooting


### Problem 1: https instead of ssh:

The symptom is:

    $ git push
    Username for 'https://github.com':

Diagnosis: the `remote` is not correct.

If you do `git remote` you get entries with `https:`:

    $ git remote -v
    origin  https://github.com/duckietown/Software.git (fetch)
    origin  https://github.com/duckietown/Software.git (push)

Expectation:

    $ git remote -v
    origin  git@github.com:duckietown/Software.git (fetch)
    origin  git@github.com:duckietown/Software.git (push)

Solution:

    $ git remote remove origin
    $ git remote add origin git@github.com:duckietown/Software.git


### Problem 1: `git push` complains about upstream

The symptom is:

    fatal: The current branch ![branch name] has no upstream branch.

Solution:

    $ git push --set-upstream origin ![branch name]

## `git` {#git status=draft}

TODO: to write


## `hub` {#hub}


### Installation

Install `hub` using the [instructions](https://hub.github.com/).

### Creating pull requests

You can create a pull request using:

    $ hub pull-request -m "![description]"
