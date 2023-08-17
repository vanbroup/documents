import os
import re
import argparse
from pathlib import Path


parser = argparse.ArgumentParser(
    description='Convert a CA/Browser Forum RFC 3647 document into small documents structured by section.')
parser.add_argument('document', type=str, help='e.g., ../docs/BR.md')
parser.add_argument('-a', '--abbreviation', type=str,
                    help='abbreviation used in filenames')
parser.add_argument('-d', '--depth', default=3, type=int,
                    help='only create directories for N levels')
parser.add_argument('-o', '--output', default='../structured/', type=str,
                    help='output directory')
parser.add_argument('-t', '--truncate', default=35, type=int,
                    help='truncate the tile at N')
args = parser.parse_args()

# Long titles can exceed the max path length, using these settings you
# can control the title truncation and until how many levels deep we
# create directories.
depth = args.depth
truncate = args.truncate
abbreviation = os.path.splitext(os.path.basename(args.document))[0]

if args.abbreviation != None:
    abbreviation = args.abbreviation

os.chdir(args.output)
output = os.getcwd()

# Read existing directory structure and map to sections to
# avoid name mismatches.
sections = {}
p = Path('../structured')
objects = sorted(p.rglob("*"))
for o in objects:
    if o.is_dir():
        if o.resolve().__str__().__contains__("APPENDIX"):
            continue

        r = re.findall("([0-9]{3}) ", o.resolve().__str__())
        if r != None:
            section = ".".join([str(item).lstrip("0") for item in r])
            sections[section] = o.resolve()

# Parse the given document
with open(args.document, 'r', encoding="utf8") as f:
    file = open(os.fsencode("000_{}.md".format(
        abbreviation)), "a", encoding="utf8")

    for line in f:
        if line.startswith("#"):
            file.close()

            # Remove duplicate spaces
            t = re.sub('\s+', ' ', line).split(" ", 2)
            title = re.sub('[^a-zA-Z0-9\- ]', ' ', t[2].strip())
            title = re.sub('\s+', ' ', title)
            title = (title[:truncate]) if len(title) > truncate else title

            section = t[1].strip(".").replace(
                "APPENDIX", "A").replace("Appendix", "A")

            n = section.split(".")
            if section in sections:
                os.chdir(sections[section])

                # open file for writing
                file = open(os.fsencode("000_{}_{}.md".format(
                    abbreviation, title)), "a", encoding="utf8")
                file.write(line)
                continue

            elif section.count('.') == 0:
                os.chdir(output)

            elif section.count('.') > depth:
                # change to directory of X sections deep
                os.chdir(sections[".".join(n[:depth])])

                # add a prefix to each file, indicating the section if we create
                # multiple sections in one directory
                si = "-".join([str(item).zfill(3) for item in n[depth:]])
                file = open(os.fsencode("{}_000_{}_{}.md".format(
                    si, abbreviation, title)), "a", encoding="utf8")
                file.write(line)
                continue

            elif ".".join(n[:-1]) in sections:
                os.chdir(sections[".".join(n[:-1])])

            else:
                print("error, don't know where I'm - {}\n".format(section))
                exit

            prefix = n[-1].zfill(3)
            if section == "A":
                prefix = "APPENDIX"

            dirname = "./{} {}".format(prefix, title)
            try:
                os.makedirs(dirname, exist_ok=True)
            except Exception as e:
                print("failed to create directory: {} in {}\n{}\n".format(
                    dirname, os.getcwd(), e))

            os.chdir(dirname)
            sections[section] = os.getcwd()

            print("{} ## {} -- {} :: {} ** {}".format(
                n[-1].zfill(3), section, title, dirname, section.__len__()))

            # open file for writing
            file = open(os.fsencode("000_{}_{}.md".format(
                abbreviation, title)), "a", encoding="utf8")
            file.write(line)

        elif line.startswith("No stipulation"):
            # do not include no stipulation statements, these can automatically be generated
            # if none of the layers stipulate any requirements
            continue

        else:
            file.write(line)
