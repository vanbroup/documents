#!/bin/sh

echo "Removing old documents"

rm -rf ../structured/*

echo "Tranforming documents"

py transform.py ../docs/BR.md
py transform.py ../docs/EVG.md
py transform.py ../docs/CS.md
py transform.py ../docs/SMIME.md

echo "Removing duplicates"

py duplicates.py > ../duplicates.md

echo "Building documents"

py build.py BR
py build.py EVG
py build.py CS
py build.py SMIME

mkdir -p ../public
py tohtml.py -out ../public/index.html

echo "Done"