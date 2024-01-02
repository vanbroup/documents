from jinja2 import Environment, FileSystemLoader
import re
import os
import argparse
from pathlib import Path
import markdown

# Define document types as constants
DOCUMENT_TYPES = ['BR', 'CS', 'SMIME', 'EVG', 'TLS']

def get_section(file: Path) -> str:
    return ".".join([str(item).lstrip("0") for item in re.findall("([0-9]{3}|[0-9]{2}[A-Z]) ", file.resolve().__str__())])

def read_markdown(filename):
    with open(filename, encoding="utf-8") as source_file:
        return source_file.read()

def markdown_to_html(markdown_text):
    # Remove front matter (assumes it starts and ends with '---')
    front_matter_pattern = re.compile(r'^---\s*\n.*?\n---\s*\n', re.DOTALL)
    markdown_text = re.sub(front_matter_pattern, '', markdown_text)

    # Use the tables extension to convert Markdown tables to HTML
    return markdown.markdown(markdown_text, extensions=['abbr', 'fenced_code', 'tables', 'toc'])

def main():
    parser = argparse.ArgumentParser(
        description='Remove files that have the same content as the Baseline Requirements')
    parser.add_argument('-in', '--input', default='../structured/', type=str,
                        help='input directory')
    parser.add_argument('-out', '--output', default='output.html', type=str,
                        help='output file name')
    args = parser.parse_args()

    sections = {}
    p = Path(args.input)
    files = sorted(p.rglob("*.md"))
    for f in files:
        rt = re.search("\_([A-Z]{2,8})(_|\.md)", f.name)
        if rt is None:
            print("Invalid filename {}".format(f.name))
            continue  # Skip invalid filenames

        type = rt.group(1)
        section = get_section(f)
        if section not in sections:
            sections[section] = {'BR': [], type: []}
        else:
            # Ensure 'type' key is present in the dictionary
            sections[section].setdefault(type, [])

        sections[section][type].append(f)

    # Load the Jinja2 template environment with 'do' extension
    env = Environment(loader=FileSystemLoader('templates'), extensions=['jinja2.ext.do'])
    
    # Pass the len and enumerate functions to the template environment
    env.globals['len'] = len
    env.globals['enumerate'] = enumerate
    env.globals['range'] = range
    
    # Include similarity/duplicate information
    similarity = ""
    with open('../duplicates.md', encoding="utf-8") as source_file:
        similarity = markdown_to_html(source_file.read())

    for dirpath, dirnames, filenames in os.walk('templates'):
        for filename in filenames:
            # Skip files in the includes directory
            if 'includes' in dirpath:
                continue

            # Get the template
            template_file = os.path.join(dirpath, filename)
            relative_template_file = os.path.relpath(template_file, 'templates')
            template = env.get_template(relative_template_file)

            # Render the template with data
            # {{ markdown_to_html(file_paths[0].read_text(encoding='utf-8')) }}
            output = template.render(
                sections=sections,
                document_types=DOCUMENT_TYPES,
                markdown_to_html=markdown_to_html,
                read_markdown=read_markdown,
                similarity=similarity
            )

            # Create the same directory structure in the output directory
            output_dir = dirpath.replace('templates', args.output)
            os.makedirs(output_dir, exist_ok=True)

            # Write the output to a file in the output directory
            with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
                f.write(output)


if __name__ == '__main__':
    main()
