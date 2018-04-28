# Setup Github access {#github-access status=ready}

Assigned: Andrea


This chapter describes how to create a Github account and setup SSH
on the robot and on the laptop.

## Create a Github account

Our example account is the following:

    Github name: greta-p
    E-mail: greta-p@duckietown.com

Create a Github account ([](#fig:github0)).

<!-- (redirects to Andrea)
    greta-p@censi.org -->

<img figure-id='fig:github0' style='width: 10em' class='github-screenshot' src='github0.png'/>

Go to your inbox and verify the email.

## Become a member of the Duckietown organization

Give the administrators your account name. They will invite you.

Accept the invitation to join the organization that you will find in your email.

## Add a public key to Github {#howto-add-pubkey-to-github}

You will do this procedure twice: once for the public key created on the laptop,
and later with the public key created on the robot.

<div class='requirements' markdown='1'>

Requires: A public/private keypair already created and configured.
This procedure is explained in [](#howto-create-key-pair).

Results: You can access Github using the key provided.

</div>

Comment: Since I am not as familiar with Linux an VIM it would have been great to say how we can get access to the public key:
sudo vim /home/username/.ssh/username@host name.pub and than copy it and add it on github
SL

Go to settings ([](#fig:github1)).

<img figure-id='fig:github1'  style='width: 10em'  class='github-screenshot'  src='github1.png'/>

Add the public key that you created:

<img figure-id='fig:github2'  style='width: 10em' class='github-screenshot'  src='github2.png'/>

<img figure-id='fig:github3'  style='width: 10em' class='github-screenshot'  src='github3.png'/>

<img figure-id='fig:github4'  style='width: 10em' class='github-screenshot'  src='github4.png'/>

<style>
.github-screenshot {
    max-width: 80%;
}
</style>


To check that all of this works, use the command

    $ ssh -T git@github.com

The command tries to connect to Github using the private keys that you specified.
This is the expected output:

    Warning: Permanently added the RSA host key for IP address '![ip address]' to the list of known hosts.
    Hi ![username]! You've successfully authenticated, but GitHub does not provide shell access.

If you don't see the greeting, stop.

Repeat what you just did for the Duckiebot on the laptop as well, making sure
to change the name of the file containing the private key.
