import re
import argparse
import string
import difflib
from pathlib import Path
from transformers import pipeline

def get_section(file: Path) -> str:
    return ".".join([str(item).lstrip("0") for item in re.findall("([0-9]{3}|[0-9]{2}[A-Z]) ", file.resolve().__str__())])

def compare_texts(text1, text2):
    # Remove punctuation, spaces, and newlines from the texts
    translator = str.maketrans('', '', string.punctuation + ' \n')
    text1_cleaned = text1.lower().translate(translator)
    text2_cleaned = text2.lower().translate(translator)

    # Use difflib to get the differences
    differ = difflib.Differ()
    differences = differ.compare(text1_cleaned, text2_cleaned)

    # Convert differences list to a string
    differences_str = ''.join(differences)

    # Use difflib to compare the cleaned texts
    similarity_ratio = difflib.SequenceMatcher(None, text1_cleaned, text2_cleaned).ratio()

    # Convert ratio to percentage
    similarity_percentage = round(similarity_ratio * 100, 2)

    return similarity_percentage, differences_str

def generate_diff_description(text1, text2):
    return ""
    # Only generate description if there are differences
    diff_generator = pipeline(task="text-generation", model="EleutherAI/gpt-neo-2.7B")
    
    # Generate a description of the differences
    diff_description = diff_generator(f"Differences between the texts:\n{text1}\n\n{text2}", max_length=300)[0]['generated_text']
    
    return diff_description

def main():
    parser = argparse.ArgumentParser(
        description='Remove files that have the same content as the Baseline Requirements')
    parser.add_argument('-in', '--input', default='../structured/', type=str,
                        help='input directory')
    args = parser.parse_args()

    sections = {}
    p = Path('../structured')
    files = sorted(p.rglob("*.md"))

    # Process BR files first to avoid re-reading them for each type
    br_files = {section: f for f in files if 'BR' in f.name and (section := get_section(f))}
    
    for f in files:
        if 'BR' not in f.name:
            type = re.search("\_([A-Z]{2,8})(_|\.md)", f.name)
            if type:
                type = type.group(1)
                section = get_section(f)
                
                if type not in sections:
                    sections[type] = {}
                
                sections[type][section] = f.resolve()

    print("| Section  | Type  | Similarity (%) | Differences |")
    print("|:---------|:-----:|:--------------:|:-----------:|")

    for section, br_file in br_files.items():
        for type, file in sections.items():
            if type != 'BR' and section in file:
                try:
                    with br_file.open(encoding="utf8") as source_file:
                        source = source_file.read()

                    with file[section].open(encoding="utf8") as copy_file:
                        copy = copy_file.read()

                    # Use difflib to compare the cleaned texts
                    similarity_percentage, _ = compare_texts(source, copy)

                    # If similarity_percentage is less than 100, generate AI description of differences
                    if similarity_percentage < 100:
                        diff_description = generate_diff_description(source, copy)
                    else:
                        diff_description = "No differences."

                    # Align the percentage column to the right
                    print("| {} | {} | {:>8} | {} |".format(section, type, similarity_percentage, diff_description))
                    
                    if similarity_percentage == 100:
                        sections[type][section].unlink()
                except Exception as e:
                    print("Error while processing files: {}".format(e))

if __name__ == '__main__':
    main()
