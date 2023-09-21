import filecmp
import re
import argparse
from pathlib import Path


def get_section(file: Path) -> str:
    return ".".join([str(item).lstrip("0") for item in re.findall("([0-9]{3}|[0-9]{2}[A-Z]) ", file.resolve().__str__())])


def main():
    parser = argparse.ArgumentParser(
        description='Remove files that have the same content as the Baseline Requirements')
    parser.add_argument('-in', '--input', default='../structured/', type=str,
                        help='input directory')
    args = parser.parse_args()

    sections = {}
    p = Path('../structured')
    files = sorted(p.rglob("*.md"))
    for f in files:
        rt = re.search("\_([A-Z]{2,8})(_|\.md)", f.name)
        if rt == None:
            print("Invalid filename {}".format(f.name))

        type = rt.group(1)
        section = get_section(f)
        if not type in sections:
            sections[type] = {}

        sections[type][section] = f.resolve()

    for section in sections['BR']:
        for type in sections:
            if type != 'BR' and section in sections[type]:
                try:
                    source = sections['BR'][section].read_text(encoding="utf8")
                    copy = sections[type][section].read_text(encoding="utf8")

                    source = re.sub(r'\s+', ' ', source).strip()
                    copy = re.sub(r'\s+', ' ', copy).strip()

                    if source == copy:
                        print("{} equal to {}".format(section, type))
                        sections[type][section].unlink()
                except Exception as e:
                    print("Error while processing files: {}".format(e))


if __name__ == '__main__':
    main()
