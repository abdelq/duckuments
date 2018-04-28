#!/usr/bin/env python
import sys, os
filename = sys.argv[1]
stylesheet = sys.argv[2]

data = open(filename).read()

path = "file://"  + os.path.realpath(stylesheet)

s = '<link rel="stylesheet" type="text/css" href="%s"/>' % path

before = '</head>'
if s in data:
    print('Already present ' + s)
else:

    data2 = data.replace(before, s+before)
    assert s in data2

    with open(filename, 'w') as f:
        f.write(data2)
