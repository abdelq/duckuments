# The Duckuments bot {#duckuments-bot status=ready}

Note: This is an advanced section mainly for Liam.

## Documentation deployment

The book is published to a different [repository called `duckuments-dist`](https://github.com/duckietown/duckuments-dist) and from there
published as `book.duckietown.org`.


## Understand what's going on

There is a bot, called `frankfurt.co-design.science`, which is an AWS machine (somewhere in Frankfurt).

Every minute, it tries to do the following:

1. It checks out the last version of `mcdp`;
1. It checks out the last version of `duckuments`;
1. It compiles the various versions;
1. It uploads the results to a repository called `duckuments-dist`.

This process takes 4 minutes for an incremental change, and about 10-15 minutes
for a big change, such as a change in headers IDs, which implies re-checking all cross-references.

<!-- 
Moreover, every 2 hours, all processes are killed, all intermediate files are deleted,
and the compilation starts from scratch. This might take about 30 minutes. -->

## Logging

There are logs you can access to see what's going on.

[The high-level compilation log][compilation] tells you in what phase of the cycle the bot is. Scroll to the bottom.

Ideally what you want to see is something like the following:

    Starting
    Mon Sep 11 10:49:04 CEST 2017
      succeded html
      succeded fall 2017
      succeded upload
      succeded split
      succeded html upload
      succeded PDF
      succeded PDF upload
    Mon Sep 11 10:54:21 CEST 2017
    Done.

This shows that the compilation took 5 minutes.

Every two hours you will see something like this:

    automatic-compile-cleanup killing everything

and the next iteration will take longer because it starts from scratch.


[The last log][last] is a live version of the compilation log. This might not be tremendously informative because it is very verbose.

[compilation]: http://frankfurt.co-design.science/~duckietown/duckuments/misc/bot/logs/fall2017/compilation.log

[last]: http://frankfurt.co-design.science/~duckietown/duckuments/misc/bot/logs/fall2017/last.log


## Debugging Github Pages problems

Sometimes, it's Github Pages that lags behind.

To check this, the bot also makes available the compilation output as a website
called `book2.duckietown.org`. You can take any URL starting with
`book.duckietown.org`, put `book2`, and you will see what is on the server.

This can identify if the problem is Github.
