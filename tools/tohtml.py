from jinja2 import Environment, FileSystemLoader
from transformers import pipeline
import re
import argparse
from pathlib import Path
import string
import markdown

# Define document types as constants
DOCUMENT_TYPES = ['BR', 'CS', 'SMIME', 'EV', 'TLS']

def get_section(file: Path) -> str:
    return ".".join([str(item).lstrip("0") for item in re.findall("([0-9]{3}|[0-9]{2}[A-Z]) ", file.resolve().__str__())])

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
    args = parser.parse_args()

    sections = {}
    p = Path('../structured')
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
    env = Environment(loader=FileSystemLoader('.'), extensions=['jinja2.ext.do'])
    
    # Pass the len and enumerate functions to the template environment
    env.globals['len'] = len
    env.globals['enumerate'] = enumerate
    
    template = env.get_template('template.html')

    # Render the template with data
    rendered_html = template.render(
        sections=sections,
        document_types=DOCUMENT_TYPES,
        markdown_to_html=markdown_to_html,
        range=range  # Pass the range function to the template
    )

    # Print the rendered HTML
    print(rendered_html)

if __name__ == '__main__':
    main()
