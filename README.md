# Text File Number Extractor

[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/gmcarelli/improved-goggles/blob/main/process_grades.py)

This repository contains a Python script, `process_grades.py`, designed to recursively scan a directory for text files (`.txt`), extract all numerical integers from them, and save the extracted numbers into corresponding CSV files.

## Description

The script provides a command-line tool to automate the process of pulling numerical data out of unstructured text files. For each `.txt` file found in a specified source directory, it creates a `.csv` file in a `results/` subdirectory. Each CSV file contains a single row with all the integer values found in its corresponding text file.

## Features

- **Integer Extraction**: Scans text files line by line to find and extract all integer values.
- **Batch Processing**: Processes all `.txt` files within a given directory.
- **Organized Output**: Saves the extracted data into CSV files within a newly created `results` directory, preserving the original filenames.
- **Error Handling**: Includes basic error handling for missing files or directories.
- **Command-Line Interface**: Easy to run from the terminal with a single directory argument.

## Prerequisites

This script is written in Python 3 and uses only standard libraries (`os`, `csv`, `argparse`). No external dependencies are required.

## Usage

1.  Clone or download the repository.
2.  Create a directory containing the text files you want to process. For example, a directory named `data` with files like `grades1.txt`, `report.txt`, etc.
3.  Run the script from your terminal, providing the path to your data directory as an argument.

```bash
python process_grades.py <path_to_your_directory>
```

### Example

Suppose you have the following directory structure:

```
.
├── process_grades.py
└── data/
    └── student_scores.txt
```

And `student_scores.txt` contains the following text:

```
Student A scored 95 on the final exam.
Student B got an 88.
Student C achieved a 72.
```

Run the script with the following command:

```bash
python process_grades.py data
```

The script will create a `results` directory and a new CSV file inside it:

```
.
├── process_grades.py
├── data/
│   └── student_scores.txt
└── results/
    └── student_scores.csv
```

The content of `results/student_scores.csv` will be:

```csv
95,88,72
