# Accessing computers using SSH {#ssh status=ready}

Assigned: Andrea

## Background reading {status=draft}

TODO: to write

- Encryption
- Public key authentication


## Installation of SSH {status=draft}

This installs the client:

    $ sudo apt install ssh

This installs the server:

TODO: to write

This enables the server:

TODO: to write

## Local configuration {#ssh-local-configuration}

The SSH configuration as a client is in the file

    ~/.ssh/config

Create the directory with the right permissions:

    $ mkdir ~/.ssh
    $ chmod 0700 ~/.ssh

Edit the file:

    ~/.ssh/config

(We suggest you use [VIM](#vim) to edit files; see a tutorial [here](http://http://www.openvim.com/).)

Comment: laptop or duckiebot? - LP

Then add the following lines:

    HostKeyAlgorithms ssh-rsa

The reason is that Paramiko, used by `roslaunch`,
[does not support the ECSDA keys][bug].

[bug]: https://answers.ros.org/question/41446/a-is-not-in-your-ssh-known_hosts-file/




## How to login with SSH and a password {#howto-login}

To log in to a remote computer `![remote]` with user `![remote-user]`, use:

    $ ssh ![remote-user]@![remote]

### Troubleshooting

**Symptom**: "Offending key error".

If you get something like this:

    Warning: the ECDSA host key for ![...] differs from the key for the IP address '![...] '

    Offending key for IP in /home/![user]/.ssh/known_hosts:![line]

then remove line `![line]` in `~/.ssh/known_hosts`.


## Creating an SSH keypair {#howto-create-key-pair}

This is a step that you will repeat twice: once on the Duckiebot, and once on your laptop.

The program will prompt you for the filename on which to save the file.

Use the convention

    /home/![username]/.ssh/![username]@![host name]
    /home/![username]/.ssh/![username]@![host name].pub

where:

- `![username]` is the current user name that you are using (`ubuntu` or your chosen one);
- `![host name]` is the name of the host (the Duckiebot or laptop);


An SSH key can be generated with the command:

    $ ssh-keygen -h

 <!--
So when you do this on the robot, use

    /home/![ubuntu]/.ssh/![username]@![robot name]

and when doing it on the laptop, use the file name:

    /home/![username]/.ssh/![username]@![laptop name] -->

The session output will look something like this:

    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/![username]/.ssh/id_rsa):

At this point, tell it to choose this file:

    /home/![username]/.ssh/![username]@![host name]

Then:

    Enter passphrase (empty for no passphrase):

Press enter; you want an empty passphrase.

    Enter same passphrase again:

Press enter.

    Your identification has been saved in /home/![username]/.ssh/![username]@![host name]
    Your public key has been saved in /home/![username]/.ssh/![username]@![host name].pub
    The key fingerprint is:
    ![XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX:XX] ![username]@![host name]
    The key's randomart image is:
    +--[ RSA 2048]----+
    |            .    |
    |       o   o  .  |
    |      o = o  . o |
    |       B . .  * o|
    |        S o    O |
    |         o o  . E|
    |          o o  o |
    |           o  +  |
    |            .. . |
    +-----------------+


Note that the program created two files.

The file that contains the private key is

    /home/![username]/.ssh/![username]@![host name]

The file that contains the public key has extension `.pub`:

    /home/![username]/.ssh/![username]@![host name].pub

Next, tell SSH that you want to use this key.

Make sure that the file `~/.ssh/config` exists:

    $ touch ~/.ssh/config

Add a line containing

    IdentityFile ~/.ssh/![PRIVATE_KEY_FILE]

(using the filename for the private key).

Comment: make sure to include the full path to the file, not just the filename.

Check that the config file is correct:

    $ cat ~/.ssh/config
    ![...]
    IdentityFile ~/.ssh/![PRIVATE_KEY_FILE]
    ![...]

To copy the generated SSH key to the clipboard xclip can be used (Installation of xclip if necessary).

    $ sudo apt-get install xclip
    $ xclip -sel clip < ~/.ssh/![username]@![host name].pub

## How to login without a password {#howto-login-without-password}


<div class='requirements' markdown='1'>

Requires: You have two computers, called "`![local]`" and "`![remote]`",
  with users "`![local-user]`" and "`![remote-user]`". Here, we assume that `![local]` and `![remote]` are complete hostnames (such as `duckiebot.local`.).

Requires: The two computers are on the same network and they can ping each other.

Requires: You have created a keypair for `![local-user]` on `![local]`.
This procedure is described in [](#howto-create-key-pair).

Results: From the `![local]` computer, `![local-user]` will be able to log in to
  `![remote]` computer without a password.

</div>

First, connect the two computers to the same network, and make sure that you
can ping `![remote]` from `![local]`:

    ![local] $ ping ![remote].local

Do not continue if you cannot do this successfully.

If you have created a keypair for `![local-user]`, you will have a public key
in this file on the `![local]` computer:

    /home/![local-user]/.ssh/![local-user]@![local].pub

This file is in the form:

    ssh-rsa ![long list of letters and numbers] ![local-user]@![local]

You will have to copy the contents of this file on the `![remote]` computer,
to tell it that this key is authorized.

On the `![local]` computer, run the command:

    ![local] $ ssh-copy-id ![remote-user]@![remote]

now you should be able to login to the remote without a password:

    ![local] $ ssh ![remote-user]@![remote]

This should succeed, and you should not be asked for a password.

## Fixing SSH Permissions {#howto-fix-ssh-permissions}

Sometimes, SSH does not work because you have the wrong permissions on some
files.

In doubt, these lines fix the permissions for your `.ssh` directory.

    $ chmod 0700 ~/.ssh
    $ chmod 0700 ~/.ssh/*



## `ssh-keygen` {#ssh-keygen status=draft}

TODO: to write
