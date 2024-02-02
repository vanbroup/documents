#!/bin/bash

echo "::group::Remove existing structured documents"
rm -rf ../structured/*
echo "::endgroup::"

echo "::group::Tranforming documents"
python transform.py ../docs/BR.md
python transform.py ../docs/EVG.md
python transform.py ../docs/CS.md
python transform.py ../docs/SMIME.md
echo "::endgroup::"

echo "::group::Change known BR TLS specific files to TLS"
find ../structured/APPENDIX/ -type f -name "000_BR_*.md" -exec bash -x -c 'mv -v "$1" "${1//_BR_/_TLS_}"' _ {} \;
echo "::endgroup::"

echo "::group::Remove duplicates"
python duplicates.py | tee ../duplicates.md
echo "::endgroup::"

echo "::group::Add examples"
cp -rv testlayers/* ../structured/
echo "::endgroup::"

echo "::group::Build documents"
python build.py BR
python build.py EVG
python build.py CS
python build.py SMIME
echo "::endgroup::"

echo "::group::Change Baseline Requirements files to TLS that should end up in the other documents"
python totls.py
echo "::endgroup::"

echo "::group::Using BR main document as a template for TLS"
cp -v ../structured/000_BR.md ../structured/000_TLS.md
sed -i 's/Certificates/TLS Certificates/g' ../structured/000_TLS.md
echo "::endgroup::"

echo "::group::Remove output"
rm -fv ../output/*
echo "::endgroup::"

echo "::group::Building documents again"
python build.py BR
python build.py EVG
python build.py CS
python build.py SMIME
python build.py TLS
echo "::endgroup::"

echo "::group::Create HTML pages"
mkdir -p ../public
python tohtml.py -out ../public/
echo "::endgroup::"

echo "Done"