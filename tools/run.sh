#!/bin/sh

echo "Removing old documents"

rm -rf ../structured/*

echo "Tranforming documents"

py transform.py ../docs/BR.md
py transform.py ../docs/EV.md
py transform.py ../docs/CS.md
py transform.py ../docs/SMIME.md

echo "Removing duplicates"

py duplicates.py > ../duplicates.md

echo "Building documents"

py build.py BR
py build.py EV
py build.py CS
py build.py SMIME

mkdir -p ../public
python3 tohtml.py > ../public/index.html

echo "Done"