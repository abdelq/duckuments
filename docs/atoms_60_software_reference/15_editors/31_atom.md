# Atom {#atom status=ready}

## Install Atom {#install-atom}

Following [the instructions here][instructions]:

    $ sudo add-apt-repository ppa:webupd8team/atom
    $ sudo apt update
    $ sudo apt install atom

[instructions]: http://tipsonubuntu.com/2016/08/05/install-atom-text-editor-ubuntu-16-04/

After installing Atom, please open it once and close it again before proceeding with installing remote-atom! 

## Using Atom to code remotely {#remote-coding}

With Atom, you are able to remotely code on files located on your Duckiebot with a GUI. The benefit of using Atom is that you are able to install extensions such as an IDE for Python, a Markdown previewer, or just use custom themes to avoid coding in the terminal.

Follow these instructions:

Install remote-atom

    laptop $ sudo apm install remote-atom
    
Now, we need to edit our SSH config so that any data send to the port 52698, which is the port remote-atom is using, is forwarded via SSH to our local machine. Edit the file "~/.ssh/config". There, you add "RemoteForward 52698 127.0.0.1:52698" to your host. The resulting host will look similar to

    Host lex
        User julien
        Hostname lex.local
        RemoteForward 52698 127.0.0.1:52698
        
Now, we need to connect to our duckiebot via SSH and install rmate (and simultaniously rename it to ratom)

    duckiebot $ sudo wget -O /usr/local/bin/ratom https://raw.github.com/aurora/rmate/master/rmate
    duckiebot $ sudo chmod +x /usr/local/bin/ratom
    
Now, you just need to launch Atom on your local machine, go to Packages->Remote Atom->Start Server.

You can now edit a file in a terminal connected to your duckiebot via SSH by typing

    duckiebot $ sudo ratom filename
    
And atom will automatically open the file on your local machine. In the settings of remote-atom, you can also set the package to start the server automatically on launching atom on your local machine.
