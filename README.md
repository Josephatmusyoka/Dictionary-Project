# Dictionary Program

## Overview
This project is a Python program that allows users to search for the definitions of words from a dictionary stored in a JSON file. It includes features like case-insensitive word search, handling of misspellings by suggesting similar words, and error handling when a word is not found.

## Features
- Load word definitions from a JSON file.
- Search for word definitions in a case-insensitive manner (e.g., `Rain`, `rain`, `RAIN`).
- Suggest the closest matching word if the user enters a misspelled word using the `difflib` library.
- Handle errors if a word is not in the dictionary by returning an appropriate message.

## How to Run the Program
1. Ensure Python 3.x is installed on your machine.
2. Download or clone the project files.
3. Navigate to the project folder in your terminal:
   ```bash
   cd dictionary_project
Run the program:
python dictionary.py
Input a word to search for its definition.