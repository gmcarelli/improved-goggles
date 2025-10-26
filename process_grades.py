"""
This script extracts numerical data from text files and saves it to CSV files.
"""

import os
import csv
from typing import List

def extract_numbers_from_file(file_path: str) -> List[int]:
    """
    Reads a text file, extracts numbers, and returns them as a list of integers.

    Args:
        file_path: The path to the text file.

    Returns:
        A list of integers found in the file.
    """
    numbers: List[int] = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                # Find all numeric strings in the line and convert them to integers
                found_numbers = [int(s) for s in line.split() if s.isdigit()]
                numbers.extend(found_numbers)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return numbers

def save_list_to_csv(numbers: List[int], input_filepath: str) -> None:
    """
    Saves a list of numbers to a CSV file.

    The output filename is derived from the input filename.

    Args:
        numbers: The list of integers to save.
        input_filepath: The path to the original input text file.
    """
    results_dir: str = "results"
    try:
        os.makedirs(results_dir, exist_ok=True)
        base_filename = os.path.basename(input_filepath)
        output_filename = f"{os.path.splitext(base_filename)[0]}.csv"
        output_filepath: str = os.path.join(results_dir, output_filename)
        with open(output_filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(numbers)
    except IOError as e:
        print(f"Error writing to file {output_filename}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def process_text_files_in_directory(directory_path: str) -> None:
    """
    Processes all text files in a given directory.

    Args:
        directory_path: The path to the directory containing text files.
    """
    if not os.path.isdir(directory_path):
        print(f"Error: Directory not found at {directory_path}")
        return

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory_path, filename)
            numbers = extract_numbers_from_file(file_path)
            if numbers:
                save_list_to_csv(numbers, file_path)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract numbers from text files and save to CSVs.")
    parser.add_argument("directory", help="The directory containing the text files.")
    args = parser.parse_args()

    process_text_files_in_directory(args.directory)
