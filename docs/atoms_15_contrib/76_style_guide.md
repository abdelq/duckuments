# Documentation style guide {#style-guide status=ready}

This chapter describes the conventions for writing the technical documentation.

## General guidelines for technical writing

The following holds for all technical writing.

- The documentation is written in correct English.

- Do not say "should" when you mean "must". "Must" and "should" have precise
  meanings and they are not interchangeable.
  These meanings are explained [in this document][rfc].

[rfc]: https://www.ietf.org/rfc/rfc2119.txt

- "Please" is unnecessary in technical documentation.

> Bad: "Please remove the SD card."

> Better: "Remove the SD card".

- Do not use colloquialisms or abbreviations.

> Bad: "The pwd is `ubuntu`."

> Better: "The password is `ubuntu`."

> Bad: "To create a ROS pkg..."

> Better: "To create a ROS package..."

- Python is capitalized when used as a name.

> Bad: "If you are using python..."

> Better: "If you are using Python..."

- Do not use emojis.

- Do not use ALL CAPS.

- Make infrequent use of **bold statements**.

- Do not use exclamation points.

## Style guide for the Duckietown documentation

- The English version of the documentation is written in American English. Please note that your spell checker might be set to British English.

Bad: behaviour

Better: behavior

Bad: localisation

Better: localization


- It's ok to use "it's" instead of "it is", "can't" instead of "cannot", etc.

- All the filenames and commands must be enclosed in code blocks using Markdown backticks.

> Bad: "Edit the ~/.ssh/config file using vi."

> Better: "Edit the `~/.ssh/config` file using `vi`."

- <kbd>Ctrl</kbd>-<kbd>C</kbd>, `ssh` etc. are not verbs.

> Bad: "<kbd>Ctrl</kbd>-<kbd>C</kbd> from the command line".

> Better: "Use <kbd>Ctrl</kbd>-<kbd>C</kbd> from the command line".

- Subtle humor and puns about duckies are encouraged.

## Writing command lines

Use either "`laptop`" or "`duckiebot`" (not capitalized, as a hostname) as the prefix for the command line.

For example, for a command that is supposed to run
on the laptop, use:

> <pre><code>lap<span>top</span> &#36; cd ~/duckietown</code></pre>

It will become:

    laptop $ cd ~/duckietown

For a command that must run on the Duckiebot, use:

> <pre><code>duckie<span>bot</span> &#36; cd ~/duckietown</code></pre>

It will become:

    duckiebot $ cd ~/duckietown

If the command is supposed to be run on both, omit the hostname:

    $ cd ~/duckietown

## Frequently misspelled words

- "Duckiebot" is always capitalized.

- Use "Raspberry Pi", not "PI", "raspi", etc.

- These are other words frequently misspelled:

    5 GHz
    WiFi

## Other conventions

When the user must edit a file, just say: "edit `/this/file`".

Writing down the command line for editing, like the following:

    $ vi /this/file

is too much detail.

(If people need to be told how to edit a file, Duckietown is too advanced for them.)

## Troubleshooting sections

Write the documentation as if every step succeeds.

Then, at the end, make a "Troubleshooting" section.

Organize the troubleshooting section as a list of symptom/resolution.

The following is an example of a troubleshooting section.

### Troubleshooting

Symptom: This strange thing happens.

Resolution: Maybe the camera is not inserted correctly. Remove and reconnect.

Symptom: This other strange thing happens.

Resolution: Maybe the plumbus is not working correctly. Try reformatting the plumbus.
