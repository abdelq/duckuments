# Special paragraphs and environments {#special-pars status=ready}

## Special paragraphs tags {#special-paragraphs}

The system supports parsing of some special paragraphs.

Note: some of these might be redundant and will be eliminated. For now,
I am documenting what is implemented.


### Special paragraphs must be separated by a line {#empty-line-before-special}

A special paragraph is marked by a special prefix.
The list of special prefixes is given in the next section.

There must be an empty line before a special paragraph;
this is because in Markdown a paragraph starts only after an empty line.

This is checked automatically, and the compilation will abort if the mistake is found.

For example, this is invalid:

    See: this book
    See: this other book

This is correct:

    See: this book

    See: this other book

Similarly, this is invalid:

    Author: author
    Maintainer: maintainer

and this is correct:

    Author: author

    Maintainer: maintainer


### Todos, task markers

    TODO: todo

TODO: todo

    TOWRITE: towrite

TOWRITE: towrite

    Task: task

Task: task

    Assigned: assigned

Assigned: assigned



### Notes and remarks

    Remark: remark

Remark: remark

    Note: note

Note: note

    Warning: warning

Warning: warning


### Troubleshooting

    Symptom: symptom

Symptom: symptom

    Resolution: resolution

Resolution: resolution

### Guidelines

    Bad: bad

Bad: bad

    Better: better

Better: better

### Questions and answers

    Q: question

Q: question

    A: answer

A: answer


### Authors, maintainers, Point of Contact

    Maintainer: maintainer

Maintainer: maintainer

    Author: author

Author: author

    Point of Contact: Point of Contact name

Point of Contact: Point of Contact name

    Slack channel: slack channel name

Slack channel: slack channel name


### References


    See: see

See: see

    Reference: reference

Reference: reference

    Requires: requires

Requires: requires

    Results: results

Results: results

    Next steps: next steps

Next steps: next steps

    Recommended: recommended

Recommended: recommended

    See also: see also

See also: see also

<style>
#special-paragraphs\:section pre {
    margin-top: 1.5em;
    margin-bottom: 0.5em;

}
</style>

## Other `div` environments {#div-environments}

For these, note the rules:

- You must include `markdown="1"`.
- There must be an empty line after the first `div` and before the closing `/div`.

### Example usage

    <div class='example-usage' markdown="1">

    This is how you can use `rosbag`:

        $ rosbag play log.bag

    </div>

<div class='example-usage' markdown="1">

This is how you can use `rosbag`:


    $ rosbag play log.bag

</div>

### Check


    <div class='check' markdown="1">

    Check that you didn't forget anything.

    </div>

<div class='check' markdown="1">

Check that you didn't forget anything.

</div>

### Requirements

    <div class='requirements' markdown="1">

    List of requirements at the beginning of setup chapter.

    </div>

<div class='requirements' markdown="1">

List of requirements at the beginning of setup chapter.

</div>

## Notes and questions {#notes-and-questions}

There are three environments: "comment", "question", "doubt",
that result in boxes that can be expanded by the user.

These are the one-paragraph forms:

    Comment: this is a comment on one paragraph.

Comment: this is a comment on one paragraph.

    Question: this is a question on one paragraph.

Question: this is a question on one paragraph.

    Doubt: I have my doubts on one paragraph.

Doubt: I have my doubts  on one paragraph.

These are the multiple-paragraphs forms:


    <div class='comment' markdown='1'>
    A comment...

    A second paragraph...
    </div>

<div class='comment' markdown='1'>
A comment...

A second paragraph...
</div>


    <div class='question' markdown='1'>
    A question...

    A second paragraph...
    </div>

<div class='question' markdown='1'>
A question...

A second paragraph...
</div>


    <div class='doubt' markdown='1'>
    A question...

    Should it not be:

        $ alternative command

    A second paragraph...
    </div>


<div class='doubt' markdown='1'>
A question...

Should it not be:

    $ alternative command

A second paragraph...
</div>
