# Liclipse {#liclipse status=ready}


## Why using IDEs

To be productive in coding, you need to have a proper IDE.

Look at how quickly you can create Python files by using an IDE ([](#fig:eclipse-capability)).
In this case, the editor is importing the required symbols.
Think about how long would it take to do it without an IDE.

<div figure-id="fig:eclipse-capability">
    <figcaption>Eclipse editor capabilities</figcaption>
    <dtvideo src="vimeo:231843714"/>
</div>


## Other alternatives

In addition to LiClipse, the one that is suggested for this class,
there exist:

* PyCharm
* Eclipse

## Installing LiClipse {#install-liclipse}

[Follow the instructions at this page][liclipse].

[liclipse]: https://www.liclipse.com/download.html

At the moment of writing, these are:

    $ wget http://www.mediafire.com/file/rwc4bk3nthtxcvv/liclipse_4.1.1_linux.gtk.x86_64.tar.gz
    $ tar xvzf liclipse_4.1.1_linux.gtk.x86_64.tar.gz
    $ sudo ln -s `pwd`/liclipse/LiClipse /usr/bin/liclipse

Now you can run it using `liclipse`:

    $ liclipse


When it runs for the first time, choose "use this as default" and click "launch".

Choose "Import-> General -> Existing project into workspace". Select the folder `~/duckietown`.

Comment: Only Import -> General -> Projects from Folder or Archive, selecting `~/duckuments` worked for me. JT

Comment: This is not about the duckuments, it's for `duckietown` - AC

If it asks about interpreters, select "auto config".

When it shows "uncheck settings that should not be changed", just click OK.


## Set shortcuts for LiClipse

Go to "window/preferences/General/Keys".

Find "print", and unbind it.

Find "Quick switch editor", and set it to <kbd>Ctrl</kbd>-<kbd>P</kbd>.
(This is now the same as Atom.)

Find "Previous tab" and assign <kbd>Ctrl</kbd>-<kbd>Shift</kbd>-<kbd>[</kbd>
(This is now the same as Atom.)

Find "Next tab" and assign <kbd>Ctrl</kbd>-<kbd>Shift</kbd>-<kbd>]</kbd>.
(This is now the same as Atom.)

Find "Show in (PyDev package explorer)" and assign <kbd>Ctrl</kbd>-<kbd>Shift</kbd>-<kbd>M</kbd>.


## Shortcuts for LiClipse

Make sure that you can do the following tasks:


- Use the global browser: Press <kbd>Cmd</kbd>-<kbd>Shift</kbd>-<kbd>T</kbd>, type "what".
It should autocomplete to `what_the_duck`. Press enter; it should jump to the file.

- Switch among open editors with <kbd>Ctrl</kbd>-<kbd>P</kbd>.

- Switch between tabs with <kbd>Ctrl</kbd>-<kbd>Shift</kbd>-<kbd>]</kbd>, -<kbd>[</kbd>.

- See the current file in the directory, using <kbd>Cmd</kbd>-<kbd>Shift</kbd>-<kbd>M</kbd>.


<col3 class='command-table labels-row1' figure-id="tab:liclipse-commands" figure-caption="Liclipse commands">
    <s>On Linux</s>
    <s>On Mac</s>
    <s></s>

    <s><kbd>Ctrl</kbd>-<kbd>Shift</kbd>-<kbd>T</kbd></s>
    <s><kbd>Cmd</kbd>-<kbd>Shift</kbd>-<kbd>T</kbd></s>
    <s>Globals browser</s>

    <s><kbd>Ctrl</kbd>-<kbd>P</kbd></s>
    <s><kbd>Cmd</kbd>-<kbd>P</kbd></s>
    <s>Quick editor switch</s>

    <s><kbd>Ctrl</kbd>-<kbd>Shift</kbd>-<kbd>[</kbd></s>
    <s><kbd>Cmd</kbd>-<kbd>Shift</kbd>-<kbd>[</kbd></s>
    <s>Previous tab (needs to be configured)</s>

    <s><kbd>Ctrl</kbd>-<kbd>Shift</kbd>-<kbd>]</kbd></s>
    <s><kbd>Cmd</kbd>-<kbd>Shift</kbd>-<kbd>]</kbd></s>
    <s>Next tab (needs to be configured)</s>

    <s><kbd>Ctrl</kbd>-<kbd>Shift</kbd>-<kbd>M</kbd></s>
    <s><kbd>Cmd</kbd>-<kbd>Shift</kbd>-<kbd>M</kbd></s>
    <s>Show in (PyDev package explorer)</s>

    <s><kbd>Ctrl</kbd>-<kbd>1</kbd></s>
    <s><kbd>Cmd</kbd>-<kbd>1</kbd></s>
    <s>Find symbol</s>


</col3>

## Other configuration for Liclipse

From the "Preferences" section, it's suggested to:

* Get rid of the minimap on the right.
* Get rid of spellchecking.


Then, there is the issue of "code completion". This is a love-it-or-hate-it
issue. The choice is yours.
