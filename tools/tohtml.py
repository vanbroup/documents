from jinja2 import Environment, FileSystemLoader
import re
import os
import argparse
from pathlib import Path
import markdown
from diff_match_patch import diff_match_patch

# Define document types as constants
output_folder = '../output/'
DOCUMENT_TYPES = sorted([os.path.splitext(file)[0] for file in os.listdir(output_folder) if file.endswith('.md')])

def get_section(file: Path) -> str:
    return ".".join([str(item).lstrip("0") for item in re.findall("(?<!_)([0-9]{3}|[0-9]{2}[A-Z])(?!_[A-Z])", file.resolve().__str__())])

def read_markdown(filename):
    with open(filename, encoding="utf-8") as source_file:
        return source_file.read()

def markdown_to_html(markdown_text):
    # Remove front matter (assumes it starts and ends with '---')
    front_matter_pattern = re.compile(r'^---\s*\n.*?\n---\s*\n', re.DOTALL)
    markdown_text = re.sub(front_matter_pattern, '', markdown_text)

    # Use the tables extension to convert Markdown tables to HTML
    return markdown.markdown(markdown_text, extensions=['abbr', 'fenced_code', 'tables', 'toc'])

def process_files(input_dir: Path, sections: dict[str, dict[str, Path]]) -> None:
    for f in sorted(input_dir.glob("*.md")):
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

    # Process all files in the subdirectories
    for subdir in sorted(input_dir.iterdir()):
        if subdir.is_dir():
            sections = process_files(subdir, sections)

    return sections

def main():
    parser = argparse.ArgumentParser(
        description='Remove files that have the same content as the Baseline Requirements')
    parser.add_argument('-in', '--input', default='../structured/', type=str,
                        help='input directory')
    parser.add_argument('-out', '--output', default='../public/', type=str,
                        help='output directory')
    args = parser.parse_args()

    sections = {}
    sections = process_files(Path(args.input), sections)

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
            relative_template_file = os.path.normpath(relative_template_file)
            relative_template_file = relative_template_file.replace("\\", "/") 
            template = env.get_template(relative_template_file)

            # Render the template with data
            # {{ markdown_to_html(file_paths[0].read_text(encoding='utf-8')) }}
            output = template.render(
                sections=sections,
                sectionPrefix='',
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

    for section in sections:
        if section.__len__() == 0:
            continue
        
        template = env.get_template('all/index.html')
        output = template.render(
            sections=sections,
            sectionPrefix=section,
            document_types=DOCUMENT_TYPES,
            markdown_to_html=markdown_to_html,
            read_markdown=read_markdown,
            similarity=similarity
        )
        sdir = os.path.join(args.output, section)
        os.makedirs(sdir, exist_ok=True)
        with open(os.path.join(sdir, "index.html"), 'w', encoding='utf-8') as f:
            f.write(output)

    template = env.get_template('includes/diff.html')

    # Writing a document diff between docs source and final build
    dmp = diff_match_patch()

    for dt in DOCUMENT_TYPES:
        try:
            sd = dt
            if dt == 'TLS':
                sd = 'BR'
            with open('../docs/'+ sd + '.md', 'r', encoding='utf-8') as source_file:
                with open('../output/'+ dt + '.md', 'r', encoding='utf-8') as build_file:
                    source_content = source_file.read()
                    build_content = build_file.read()
                    if source_content != build_content:
                        diffs = dmp.diff_main(source_content, build_content)
                        dmp.diff_cleanupSemantic(diffs)

                        diff_html = dmp.diff_prettyHtml(diffs)

                        # Calculate similarity
                        levenshtein = dmp.diff_levenshtein(diffs)
                        diff_similarity = (1 - levenshtein / max(len(source_content), len(build_content))) * 100

                    else:
                        diff_html = "The input and output are exactly the same."

                    rendered_html = template.render(
                        document_types=DOCUMENT_TYPES,
                        document_type=dt,
                        markdown_to_html=markdown_to_html,
                        source_content=source_content,
                        build_content=build_content,
                        diff_text=diff_html,
                        diff_similarity=diff_similarity,
                        range=range  # Pass the range function to the template
                    )

                    with open(args.output+'/diff-'+ dt.lower() +'.html', 'w', encoding='utf-8') as output_file:
                        output_file.write(rendered_html)
        except FileNotFoundError as e:
            print(f"File not found: {e.filename}")
        except Exception as e:
            print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    main()
