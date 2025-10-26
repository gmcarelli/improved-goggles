"""
This script extracts numerical data from text files and saves it to CSV files.
"""

import csv
from pathlib import Path
from typing import List

def extract_numbers_from_file(file_path: Path) -> List[int]:
    """
    Reads a text file, extracts numbers, and returns them as a list of integers.

    Args:
        file_path: The path to the text file.

    Returns:
        A list of integers found in the file.
    """
    numbers: List[int] = []
    try:
        with file_path.open('r', encoding='utf-8') as f:
            for line in f:
                # Find all numeric strings in the line and convert them to integers
                found_numbers = [int(s) for s in line.split() if s.isdigit()]
                numbers.extend(found_numbers)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return numbers

def save_list_to_csv(numbers: List[int], input_filepath: Path) -> None:
    """
    Saves a list of numbers to a CSV file.

    The output filename is derived from the input filename.

    Args:
        numbers: The list of integers to save.
        input_filepath: The path to the original input text file.
    """
    results_dir = Path("results")
    try:
        results_dir.mkdir(exist_ok=True)
        output_filename = input_filepath.stem + ".csv"
        output_filepath = results_dir / output_filename
        with output_filepath.open('w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(numbers)
    except IOError as e:
        print(f"Error writing to file {output_filename}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def process_text_files_in_directory(directory_path: Path) -> None:
    """
    Processes all text files in a given directory.

    Args:
        directory_path: The path to the directory containing text files.
    """
    if not directory_path.is_dir():
        print(f"Error: Directory not found at {directory_path}")
        return

    for file_path in directory_path.glob("*.txt"):
        numbers = extract_numbers_from_file(file_path)
        if numbers:
            save_list_to_csv(numbers, file_path)

if __name__ == "__main__":
    # Set the input directory directly for IDE-based execution
    input_dir = Path(r'sample_texts')
    process_text_files_in_directory(input_dir)
