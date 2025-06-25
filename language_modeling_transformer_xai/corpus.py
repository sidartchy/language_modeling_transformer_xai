import os
from pathlib import Path
from config import PROJ_ROOT, DATA_DIR, RAW_DATA_DIR

def merge_text_files(root_dir, output_filename="corpus.txt"):
    """
    Merges all .txt files from a root directory and its subdirectories
    into a single output corpus file.

    Args:
        root_dir (str): The path to the root directory containing the text files.
        output_filename (str): The name of the output corpus file.
    """
    corpus_content = []

    print(f"Starting to merge text files from '{root_dir}'...")

    if not os.path.isdir(root_dir):
        print(f"Error: The directory '{root_dir}' does not exist.")
        return

    # Walk through the directory and its subdirectories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".txt"):
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Add a clear separator and the file path for readability in the corpus
                        corpus_content.append(content)
                    print(f"Successfully read: {file_path}")
                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    # Write all collected content to the output file
    try:
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            outfile.write("".join(corpus_content))
        print(f"\nAll .txt files merged successfully into '{output_filename}'")
    except Exception as e:
        print(f"Error writing to output file '{output_filename}': {e}")

# --- How to use the script ---
if __name__ == "__main__":
    # Define the root directory where your 'raw' folder is located.
    # If the script is in the same directory as 'raw', just use 'raw'.
    # Otherwise, provide the full path, e.g., '/Users/yourname/Documents/raw'
    root_directory_to_scan = RAW_DATA_DIR
    output_corpus_file = f"{DATA_DIR}/processed/corpus.txt"

    merge_text_files(root_directory_to_scan, output_corpus_file)
