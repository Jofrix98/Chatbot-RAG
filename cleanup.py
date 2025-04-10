import os
import sys

def clean_markdown_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                clean_file(file_path)

def clean_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # Find the index of the first occurrence of either "## Usted está aquí" or "## Esteu aquí"
    start_index = next((i for i, line in enumerate(lines) if "## Usted está aquí" in line or "## Esteu aquí" in line or "## You are here" in line), None)
    
    if start_index is not None:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(lines[start_index:])  # Keep content from the found heading onward

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_md.py <directory>")
        sys.exit(1)
    
    target_directory = sys.argv[1]
    
    if not os.path.isdir(target_directory):
        print(f"Error: '{target_directory}' is not a valid directory.")
        sys.exit(1)

    clean_markdown_files(target_directory)
    print("Processing complete!")
