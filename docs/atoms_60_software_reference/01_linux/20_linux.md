# GNU/Linux general notions {#linux-general status=draft}

Assigned: Andrea

## Background reading

- UNIX
- Linux
- free software; open source software.

<!--

### Can you do the following?

- Log in the Duckiebot from the laptop;
- Log in the Duckiebot from the laptop, without using password;


### Can you do the following?

- Copy a file from the Duckiebot to the laptop;
- Copy a file from the laptop to the Duckiebot; -->




# Every-day Linux {#every-day-linux status=draft}


## `man` {#man}

This is an interface to the on-line reference manuals. Whenever you meet some unfamiliar commands, try use `man certain_command` before Googling. You will find it extremely clear, useful and self-contained. 

## `cd` {#cd}

Go to the directory you want. If you just use:

    laptop $ cd

then you will go to your home directory, i.e., ~

## `sudo` {#sudo}

Whenever you want to modify system files, you will need `sudo`. Commonly touched system files including `/etc`, `/opt` and so on. Since most of you have followed the guideline to use passwordless sudo, I would recommend that make sure what you are doing with sudo before you execute the command, otherwise you may need to reinstall the system. 

## `ls` {#ls}

List all the files and documents in the current directory. From `~/.bashrc`, we know some commonly used alias. See more by `man ls`. 

-- `la` for `ls -a` which will list out all files and documents including the hidden ones(whose name starts with a dot).

-- `ll` for `ls -l` which will display Unix file types, permissions, number of hard links, owner, group, size, last-modified date and filename.

## `cp` {#cp}

`cp fileA directoryB` will copy the file A to directory B. See more by executing `man cp`.

## `mkdir` {#mkdir}

Make new directory. See more by `man mkdir`.

## `touch` {#touch}

Update the access and modification times of the input file to current time. See more by `man touch`.

## `reboot` {#reboot}

This command must be executed as root. `sudo` required. This will reboot your laptop or Raspberry Pi. See more by `man reboot`.

## `shutdown` {#shutdown}

This command requires `sudo`. You can set a countdown to shutdown you machine. More by `man shutdown`.


## `rm` {#rm}

Remove certain file. `rm -r` will remove files. More in `man rm`.

# Users {#users-management status=draft}



## `passwd` {#passwd}

Update password of the current user. Old password needed. 

# UNIX tools {#unix-tools status=draft}


## `cat` {#cat}

Cat some file will return you the content. More in `man cat`. 


## `tee` {#tee}

Read from standard input and write to standard output and files. More on `man tee`. 

## `truncate` {#truncate}

TODO: to write

# Linux disks and files {#linux-disk-and-files status=draft}

## `fdisk` {#fdisk}

TODO: to write


## `mount` {#mount}

TODO: to write

## `umount` {#umount}

TODO: to write


## `losetup` {#losetup}

TODO: to write


## `gparted` {#gparted}

TODO: to write


## `dd` {#dd}

TODO: to write


## `sync` {#sync}

TODO: to write


## `df` {#df}

TODO: to write

## How to make a partition {#how-to-partition status=draft}

TODO: to write

# Other administration commands {#linux-other-admin status=draft}


## `visudo` {#visudo}

TODO: to write

## `update-alternatives` {#update-alternatives}

TODO: to write

## `udevadm` {#udevadm}

TODO: to write

## `systemctl` {#systemctl}

TODO: to write



# Make {#gnu-make status=draft}

## `make` {#make}

TODO: to write


# Python-related tools {#python-tools status=draft}

## `virtualenv` {#virtualenv}

TODO: to write

## `pip` {#pip}

TODO: to write


# Raspberry-PI commands {#RPI-commands status=draft}

## `raspi-config` {#raspi-config}

TODO: to write

## `vcgencmd` {#vcgencmd}

TODO: to write

## `raspistill` {#raspistill}

TODO: to write


## `jstest` {#jstest}

TODO: to write

## `swapon` {#swapon}

TODO: to write

## `mkswap` {#mkswap}

TODO: to write



# Users and permissions {#users-and-permissions status=draft}

## `chmod` {#chmod}

TODO: to write

## `groups` {#groups}

TODO: to write

## `adduser` {#adduser}

TODO: to write

## `useradd` {#useradd}

TODO: to write


# Downloading {#download-utils status=draft}


## `curl` {#curl}

TODO: to write


## `wget` {#wget}

TODO: to write


## `sha256sum` {#sha256sum}

TODO: to write


## `xz` {#xz}

TODO: to write

# Shells and environments {#linux-shells status=draft}

## `source` {#source}

You can only do `source file_name` if the file can be executed by bash. 

## `which` {#which}

Tell you the /bin/ directory of your command. This is useful to distinguish which python you are using if you have virtualenv. 

## `export` {#export}

TODO: to write

# Other misc commands {#linux-misc status=draft}


## `pgrep`

TODO: to write


## `npm` {#npm}

TODO: to write


## `nodejs` {#nodejs}

TODO: to write


## `ntpdate` {#ntpdate}

TODO: to write


## `chsh` {#chsh}

TODO: to write


## `echo` {#echo}

TODO: to write


## `sh` {#sh}

TODO: to write

## `fc-cache` {#fc-cache}

TODO: to write


# Mounting USB drives {#mounting-usb status=ready}

First **plug in the USB drive** nothing will work if you don't do that first. Now ssh into your robot. On the command line type:

    duckiebot $ lsusb

you should see your Sandisk USB drive as an entry. Congrats, you correctly plugged it in

    duckiebot $ lsblk

Under name you should see `sda1`, with size about 28.7GB and nothing under the `MOUNTPOINT` column (if you see something under `MOUNTPOINT` congrats you are done.

Next make a directory to mount to:

    duckiebot $ sudo mkdir /media/logs

Next mount the drive

    duckiebot $ sudo mount -t vfat /dev/sda1 /media/logs -o umask=000

Test by running `lsblk` again and you should now see `/media/logs` under `MOUNTPOINT`

## Unmounting a USB drive {#unmount-usb}

    duckiebot $ sudo umount /media/logs
