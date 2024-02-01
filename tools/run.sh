#!/bin/sh

echo "Removing old documents"

rm -rf ../structured/*

echo "Tranforming documents"

python transform.py ../docs/BR.md
python transform.py ../docs/EVG.md
python transform.py ../docs/CS.md
python transform.py ../docs/SMIME.md

echo "Change known BR TLS specific files to TLS"
find ../structured/APPENDIX/ -type f -name "000_BR_*.md" -exec sh -x -c 'mv "$1" "${1//_BR_/_TLS_}"' _ {} \;

echo "Removing duplicates"

python duplicates.py > ../duplicates.md

echo "Adding examples"
cp -r testlayers/* ../structured/

echo "Building documents"

python build.py BR
python build.py EVG
python build.py CS
python build.py SMIME

echo "Change Baseline Requirements files to TLS that should end up in the other documents"
python totls.py

echo "Using BR main document as a template for TLS"
cp ../structured/000_BR.md ../structured/000_TLS.md
sed -i 's/Certificates/TLS Certificates/g' ../structured/000_TLS.md

echo "Building documents again"
rm -f ../output/*

python build.py BR
python build.py EVG
python build.py CS
python build.py SMIME
python build.py TLS

mkdir -p ../public
python tohtml.py -out ../public/

echo "Done"