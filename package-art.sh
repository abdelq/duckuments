#!/bin/bash
set -e -x
dest="dest"
out=$1
rm -rf ${dest}

mkdir -p ${dest}/
# cp -R out/compilation/split/ ${dest}/out
# cp out/compilation/out.html ${dest}/out.html
# cp out/compilation/out.pdf ${dest}/out.pdf

cp -R duckuments-dist/* ${dest}

tar cvfz  ${out} -C dest .

