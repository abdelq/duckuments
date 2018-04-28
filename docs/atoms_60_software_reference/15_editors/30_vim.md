
# VIM {#vim status=ready}

Assigned: Andrea


To do quick changes to files, especially when logged remotely,
we suggest you use the VI editor, or more precisely, VIM ("VI iMproved").

## External documentation

See: [A VIM tutorial](http://www.openvim.com/).

## Installation

Install like this:

    $ sudo apt install vim


## `vi` {#vi status=draft}

TODO: to write

## Suggested configuration

Suggested `~/.vimrc`:

    syntax on
    set number
    filetype plugin indent on
    highlight Comment ctermfg=Gray
    autocmd FileType python set complete isk+=.,(


<!-- autocmd FileType python set complete+=k~/.vim/syntax/python.vim isk+=.,( -->

## Visual mode {status=draft}

TODO: to write

## Indenting using VIM

Use the <kbd>&gt;</kbd> command to indent.

To indent 5 lines,  use
 <kbd>5</kbd>
 <kbd>&gt;</kbd>
 <kbd>&gt;</kbd>.

To mark a block of lines and indent it, use <kbd>V</kbd>.

For example, use <kbd>V</kbd><kbd>J</kbd><kbd>J</kbd><kbd>&gt;</kbd> to indent 3 lines.

Use <kbd>&lt;</kbd> to dedent.
