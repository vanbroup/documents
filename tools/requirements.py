import re
import argparse
from pathlib import Path
import openai

# Define the prompt as a placeholder
PROMPT = """
Identify and articulate requirements from the paragraph in the CA/Browser Forum Baseline Requirements.

- Only include one requirement on each line;
- Try to answer who what and why within the requirement;
- Include the RFC 2119 key words to indicate the requirement level;
- Write unambiguous and clear requirements;
- It's fine to use comment PKI related abbreviations such as CP, CPS, CRL, OCSP, etc.;
- Requirements should be brief (about 100 characters) but comprehensive;
- Requirements should be verifiable/auditable;
- Requirements should be clear on their own;
- The subject of the requirement must be included, do not write "the document" but reference the name of the applicable document instead;
- Include actions to make requirements verifiable/auditable in the original requirement;

Write the requirements as below, including prefixed spacing, do not include any other messages in the output:

    [001] This is an example requirement

This is the paragrpah of the CA/Browser Forum Basline Requirements:

{content}
"""

def get_section(file: Path) -> str:
    return ".".join([str(item).lstrip("0") for item in re.findall("(?<!_)([0-9]{3}|[0-9]{2}[A-Z])(?!_[A-Z])", file.resolve().__str__())])

def get_requirements(content):
    completion = openai.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[{
            "role": "user", 
            "content": PROMPT.format(content=content),
        }],
    )

    return completion.choices[0].message.content.strip()

def main():
    parser = argparse.ArgumentParser(
        description='Remove files that have the same content as the Baseline Requirements')
    parser.add_argument('-in', '--input', default='../structured/', type=str,
                        help='input directory')
    args = parser.parse_args()

    p = Path(args.input)
    files = sorted(p.rglob("*.md"))

    for file in files:
        try:
            with file.open(encoding="utf8") as file_content:
                content = file_content.read()

            # TODO: Skip if there is only a title
            
            # Skip sectionn as it does not contain any requirements
            section = get_section(file)
            if section.startswith("1"):
                continue

            # Delete existing requirements
            content = re.sub("\s+\[([0-9]{3})\]\s([^$]+)\n", '', content).strip()

            requirements = get_requirements(content)

            print(requirements)

            content += f"\n\n{requirements}"

            # Write the updated content back to the file
            with file.open(mode="w", encoding="utf8") as updated_file:
                updated_file.write(content)

        except Exception as e:
            print(f"Error while processing file {file}: {e}")

if __name__ == '__main__':
    main()
