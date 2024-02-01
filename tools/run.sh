#!/bin/sh

echo "Removing old documents"

rm -rf ../structured/*

echo "Tranforming documents"

py transform.py ../docs/BR.md
py transform.py ../docs/EVG.md
py transform.py ../docs/CS.md
py transform.py ../docs/SMIME.md

echo "Change known BR TLS specific files to TLS"
find ../structured/APPENDIX/ -type f -name "000_BR_*.md" -exec sh -c 'mv "$1" "${1//_BR_/_TLS_}"' _ {} \;

echo "Removing duplicates"

py duplicates.py > ../duplicates.md

echo "Adding examples"
cp -r testlayers/* ../structured/

echo "Building documents"

py build.py BR
py build.py EVG
py build.py CS
py build.py SMIME

echo "Change Baseline Requirements files to TLS that should end up in the other documents"
py totls.py

echo "Using BR main document as a template for TLS"
cp ../structured/000_BR.md ../structured/000_TLS.md
sed -i 's/Certificates/TLS Certificates/g' ../structured/000_TLS.md

echo "Building documents again"
rm -f ../output/*

py build.py BR
py build.py EVG
py build.py CS
py build.py SMIME
py build.py TLS

mkdir -p ../public
py tohtml.py -out ../public/

echo "Done"