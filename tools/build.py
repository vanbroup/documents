import os
import io
import csv
import re
import argparse
from pathlib import Path
import frontmatter


def get_section(file: Path) -> str:
    return ".".join([str(item).lstrip("0") for item in re.findall("([0-9]{3}|[0-9]{2}[A-Z]) ", file.resolve().__str__())])


def process_files(target_type: str, loa: list[str], out: io.TextIOWrapper, req: csv.writer, input_dir: Path, sections: dict[str, Path]) -> None:
    """Processes all files in the `input_dir` directory and subdirectories, and combines them into a single file in the `output_dir` directory.

    Args:
        target_type: The target type of the combined document.
        loa: The level of assurance.
        out: The combined output file.
        req: The requirements file.
        input_dir: The input directory.
        sections: A dictionary of section names to file paths.
    """

    for f in sorted(input_dir.glob("*.md")):
        section = get_section(f)

        # Skip BR sections that have a file that overrules the BR (i.e., 000_)
        if re.match("[0-9]{3}_BR", f.name):
            if section in sections:
                continue

        elif not f.name.__contains__("_{}".format(target_type)):
            # Skip all files that are not of the target type or BR
            continue

        process_file(f, target_type, loa, out, req, sections)

    # Process all files in the subdirectories
    for subdir in sorted(input_dir.iterdir()):
        if subdir.is_dir():
            process_files(target_type, loa, out, req, subdir, sections)


def process_file(file: Path, target_type: str, loa: list[str], out: io.TextIOWrapper, req: csv.writer, sections: dict[str, Path]) -> None:
    """Processes a single file and combines it into the target file.

    Args:
        file: The file to process.
        target_type: The target type of the combined document.
        loa: The level of assurance.
        out: The combined output file.
        req: The requirements file.
        sections: A dictionary of section names to file paths.
    """
    file_loa = ''
    section = get_section(file)

    with open(file, 'r', encoding="utf8") as f:
        for line in f:
            # If this file contains frontmatter (don't check the root files)
            if line == '---\n' and not re.match("000_[A-Z]+\.md", file.name):
                fm = line
                for line in f:
                    fm += line
                    if line == '---\n':
                        break

                metadata, _ = frontmatter.parse(fm)

                # Check if any target constraints are given to include or exclude this file for
                # for the current target.
                if 'targets' in metadata:
                    if 'excluded' in metadata['targets'] and target_type in metadata['targets']['excluded']:
                        print("Skipping file '{}' in section {} as it's excluded in frontmatter".format(
                            file.name, section))
                        return
                    if 'included' in metadata['targets'] and not target_type in metadata['targets']['included']:
                        print("Skipping file '{}' in section {} as it's not included in frontmatter".format(
                            file.name, section))
                        return

                # Check if the given LoA are included or excluded
                if 'loa' in metadata:
                    file_loa = metadata['loa']

                    if not metadata['loa'] in loa:
                        print("Skipping file '{}' in section {} as LoA '{}' is not requested, only want LoA {}".format(
                            file.name, section, metadata['loa'], loa))
                        return

                continue

            if line.startswith('#'):
                # Extract the current context
                title = line.split(" ", 2)[2].strip()
                section = line.split(" ", 2)[1].strip(".")

            # Check if this line defines a requirement
            r = re.fullmatch("\s+\[([0-9]{3})\]\s([^$]+)", line)
            if r != None:
                id = f"{target_type}-{section}-{r.group(1)}"
                requirement = r.group(2).strip()
                req.writerow([id, section, file_loa, target_type, requirement])

                out.write("\t[{}] {}\n".format(id, requirement))
                continue

            out.write(line)


def main():
    """The main function."""

    parser = argparse.ArgumentParser(
        description='Combine the structured documents into one document and extract requirements')
    parser.add_argument('target_type', type=str, help='e.g., BR')
    parser.add_argument('-o', '--output', default='../output/', type=str,
                        help='output directory')
    parser.add_argument('-i', '--input', default='../structured/', type=str,
                        help='input directory')
    parser.add_argument('-l', '--loa', nargs='*', default=['DV', 'OV', 'EV'], type=str,
                        help='level of assurance')
    args = parser.parse_args()

    target_type = args.target_type
    output_dir = Path(args.output)
    input_dir = Path(args.input)
    loa = args.loa
    sections = {}

    combined_output_file = output_dir / f"{target_type}.md"
    requirements_file = output_dir / f"{target_type}_requirements.csv"

    with open(combined_output_file, "w", encoding="utf8") as out, open(requirements_file, "w", encoding="utf8", newline='') as rf:
        req = csv.writer(rf, quoting=csv.QUOTE_ALL)
        req.writerow(['ID', 'Section', 'LoA', 'Type', 'Requirement'])

        # Index all sections for the target document type
        if target_type != "BR":
            for f in sorted(input_dir.rglob("*.md")):
                if not f.name.__contains__("000_{}".format(target_type)):
                    continue

                section = get_section(f)
                sections[section] = f.resolve()

        process_files(target_type, loa, out, req, input_dir, sections)


if __name__ == '__main__':
    main()
