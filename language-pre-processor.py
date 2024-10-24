import os
import sys
import argparse

def get_available_languages() -> list[str]:
    languages_dir = os.path.join(os.path.dirname(__file__), 'languages')
    return [name for name in os.listdir(languages_dir) if os.path.isdir(os.path.join(languages_dir, name))]

def main() -> int:
    languages = get_available_languages()
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--file", type=str, required=True)
    parser.add_argument("--language", type=str, required=True, choices=languages)
    parser.add_argument("--output-file-name", type=str, required=True)
    
    arguments = parser.parse_args(sys.argv[1:])
    
    output_file_content = \
    f"""\\def\\cvlanguage{arguments.language}
\\input{arguments.file}"""

    with open(arguments.output_file_name, 'w') as output_file:
        output_file.write(output_file_content)
        
    return 0

if __name__ == "__main__":
    main()