import os
import csv
import re
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    description='Combine the structured documents into one document and extract requirements')
parser.add_argument('target', type=str, help='e.g., BR')
parser.add_argument('-o', '--output', default='../output/', type=str,
                    help='output directory')
parser.add_argument('-in', '--input', default='../structured/', type=str,
                    help='input directory')
args = parser.parse_args()

target = args.target

# combined output file
out = open("{}/{}.md".format(args.output, target), "w", encoding="utf8")

rf = open("{}/{}_requirements.csv".format(args.output,
          args.target), "w", encoding="utf8", newline='')
req = csv.writer(rf, quoting=csv.QUOTE_ALL)
req.writerow(['ID', 'Section', 'LoA', 'Type', 'Requirement'])

title = ""
section = ""

# Register files that overrule the baseline requirements
sections = {}
p = Path('../structured')
files = sorted(p.rglob("*.md"))
for f in files:
    # register all overruling files for the targeting type
    if not f.name.__contains__("000_{}".format(target)):
        continue

    elif f.resolve().__str__().find("APPENDIX"):
        continue

    # determine section
    r = re.findall("([0-9]{3}) ", f.resolve().__str__())
    if r != None:
        section = ".".join([str(item).lstrip("0") for item in r])
        sections[section] = f.resolve()

# Start combining all files for the target type document
p = Path('../structured')
files = sorted(p.rglob("*.md"))
for f in files:
    # skip BR sections if the target type has a file that overrules
    if re.match("[0-9]{3}_BR", f.name):
        # determine section
        r = re.findall("([0-9]{3}) ", f.resolve().__str__())
        if r != None:
            section = ".".join([str(item).lstrip("0") for item in r])
            if section in sections:
                continue

    # also skip all types that are not indicated
    # TODO: allow multiple types to handle combinations
    elif not f.name.__contains__("_{}".format(target)):
        continue

    rt = re.search("\_([A-Z]{2,8})(_|\.md)", f.name)
    if rt == None:
        print("Invalid filename {}".format(f.name))

    type = rt.group(1)

    # if file starts with weight is 00, don't include the another type
    with open(f.resolve(), 'r', encoding="utf8") as f:
        last_line = ""
        for line in f:
            last_line = line
            out.write(line)

            # Extract the current context
            if line.startswith("#"):
                t = line.split(" ", 2)
                title = t[2].strip()
                section = t[1].strip(".")

            # For the following to do's we need to considering multiple layers, we might need
            # another round of processing when this combined file is generated.
            # TODO: Handle/add "No stipulation"

            # Check if this line defines a requirement
            r = re.fullmatch("\s+\[([0-9]{3})\]\s([^$]+)", line)
            if r != None:
                print(
                    "***************** Identified requirement in {}:\n\t{}".format(f.name, line))

                id = "{}-{}-{}".format(type, section, r.group(1))

                # TODO: How do we handle requirements applicable to multiple levels of assurance or to multiple certificate types (e.g., DNS names, E-Mail addresses), for organization validation we include this in the LoA
                # TODO: Do we want to include the main chapter (e.g., Introduction) and section (e.g., Revisions) to give a better context?
                req.writerow([id, section, '', type, r.group(2).strip()])

