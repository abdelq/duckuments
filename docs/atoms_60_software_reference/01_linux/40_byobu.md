# Byobu {#byobu status=ready}

Assigned: Andrea

You need to learn to use Byobu. It will save you much time later.

(Alternatives such as [GNU Screen][web-screen] are fine as well.)

[web-screen]: https://en.wikipedia.org/wiki/GNU_Screen

## Advantages of using Byobu {status=draft}

TODO: To write

## Installation

On Ubuntu, install using:

    $ sudo apt install byobu

## Documentation

See also: See the screencast on the website [http://byobu.co/][web-byobu].

[web-byobu]: http://byobu.co/

## Quick command reference

You can change the escape sequence from <kbd>Ctrl</kbd>-<kbd>A</kbd> to
something else by using the configuration tool that appears when you type
<kbd>F9</kbd>.

Commands to use windows:

<col3 class='command-table labels-row1' figure-id="tab:commands-windows" figure-caption="Windows">
    <s></s>
    <s>Using function keys</s>
    <s>Using escape sequences</s>

    <s>Create new window</s>
    <s><kbd>F2</kbd></s>
    <s><kbd>Ctrl</kbd>-<kbd>A</kbd> then <kbd>C</kbd></s>

    <s>Previous window</s>
    <s><kbd>F3</kbd></s>
    <s></s>

    <s>Next window</s>
    <s><kbd>F4</kbd></s>
    <s></s>

    <s>Switch to window </s>
    <s></s>
    <s><kbd>Ctrl</kbd>-<kbd>A</kbd> then a number</s>

    <s>Close window</s>
    <s><kbd>Ctrl</kbd>-<kbd>F6</kbd></s>
    <s></s>

    <s>Rename window </s>
    <s></s>
    <s><kbd>Ctrl</kbd>-<kbd>A</kbd> then <kbd>,</kbd></s>
</col3>


Commands to use panes (windows split in two or more):

<col3 class='command-table labels-row1' figure-id="tab:commands-panes">

    <figcaption>Commands for panes</figcaption>

    <s></s>
    <s>Using function keys</s>
    <s>Using escape sequences</s>

    <s>Split horizontally</s>
    <s><kbd>Shift</kbd>-<kbd>F2</kbd></s>
    <s><kbd>Ctrl</kbd>-<kbd>A</kbd> then <kbd>|</kbd></s>

    <s>Split vertically</s>
    <s><kbd>Ctrl</kbd>-<kbd>F2</kbd></s>
    <s><kbd>Ctrl</kbd>-<kbd>A</kbd> then <kbd>%</kbd></s>

    <s>Switch focus among panes</s>
    <s><kbd>Ctrl</kbd>-<kbd>↑↓←→</kbd></s>
    <s><kbd>Ctrl</kbd>-<kbd>A</kbd> then one of
    <kbd>↑↓←→</kbd>

     </s>

    <s>Break pane</s>
    <s></s>
    <s><kbd>Ctrl</kbd>-<kbd>A</kbd> then <kbd>!</kbd></s>
</col3>

<!-- (<kbd>↑</kbd>,<kbd>↓</kbd>,<kbd>←</kbd>,<kbd>→</kbd>) -->

Other commands:


<col3 class='command-table labels-row1' figure-id="tab:commands-other" figure-caption="Other">
    <s></s>
    <s>Using function keys</s>
    <s>Using escape sequences</s>


    <s>Help </s>
    <s></s>
    <s><kbd>Ctrl</kbd>-<kbd>A</kbd> then <kbd>?</kbd></s>

    <s>Detach </s>
    <s></s>
    <s><kbd>Ctrl</kbd>-<kbd>A</kbd> then <kbd>D</kbd></s>



</col3>


<style>
.command-table td {
    text-align: left;
    font-size: 80%;
}
</style>

## Commands on OS X

Scroll up and down using
<kbd>fn</kbd><kbd>option</kbd><kbd>↑</kbd>
and
<kbd>fn</kbd><kbd>option</kbd><kbd>↓</kbd>.


Highlight using <kbd>alt</kbd>

<!-- Shift+<arrow keys> switches between panes. Shift+Alt+<arrow keys> changes the current pane size. -->

<!-- Byobu tips: don't forget F2 (or ctrl-a C) in byobu will open a terminal in a new tab. Alternatively, you can also Shift+F2 to split the current tab into two horizontally. -->
