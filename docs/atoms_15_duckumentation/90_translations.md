# Translations {#duckuments-translations status=draft}

Note: This part is not implemented yet.


## File organization

Translations are organized file-by-file.

For every file `![name].md`, name the translated file `![name].![language code].md`,
where the language code is one of the standard codes, and put it in the same directory.

For example, these could be a set of files, including a Chinese (simplified), italian,
and Spanish translation:

    representations.md
    representations.zh-CN.md
    representations.it.md
    representations.es.md

The reason is that in this way you can check automatically from Git whether `representations.zh-CN.md` is up to date or `representations.md` has been modified since.

## Guidelines for English writers

Here are some considerations for the writers of the original version, to make
the translators' job easier.

It is better to keep files smallish so that (1) the translation tasks can feel approachable by translators; (2) it is easier for the system to reason about the files.

Name all the headers with short, easy identifiers, and never change them.


## File format

All files are assumed to be encoded in UTF-8.

The header IDs should not be translated and should remain exactly the same. This will allow
keeping track of the different translations.

For example, if this is the original version:

    # Robot uprising {#robot-uprising}

    Hopefully it will never happen.

Then the translated version should be:

    # La rivolta dei robot {#robot-uprising}

    Speriamo che non succeda.
