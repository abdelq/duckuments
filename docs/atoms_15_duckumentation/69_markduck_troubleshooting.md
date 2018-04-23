# Markduck troubleshooting {#markduck-troubleshooting status=ready}

## Changes don't appear on the website

For these issues, see [](#duckuments-bot).

## Troubleshooting errors in the compilation process

Symptom: "Invalid XML"

Resolution: "Markdown" doesn't mean that you can put anything in a file. Except
for the code blocks, it must be valid XML. For example, if you use
"<code>&gt;</code>" and "<code>&lt;</code>" without quoting, it will likely
cause a compile error.

Symptom: "Tabs are evil"

Resolution: Do not use tab characters. The error message in this case is quite
helpful in telling you exactly where the tabs are.


Symptom: The error message contains `ValueError: Suspicious math fragment 'KEYMATHS000ENDKEY'`

Resolution: You probably have forgotten to indent a command line by at least 4 spaces. The dollar in the command line is now being confused for a math formula.


## Common mistakes with Markdown {#common-markdown-mistakes}

Here are some common mistakes encountered.

### Not properly starting a list {#invalid-list}

There must be an empty line before the list starts.

This is correct:

    I want to learn:

    - robotics
    - computer vision
    - underwater basket weaving

This is incorrect:

    I want to learn:
    - robotics
    - computer vision
    - underwater basket weaving

and it will be rendered as follows:

I want to learn:
- robotics
- computer vision
- underwater basket weaving
