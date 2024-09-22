import json
import difflib

# Load the dictionary data from a JSON file
def load_dictionary(file_path):
    try:
        with open(file_path, 'r') as f:
            dictionary_data = json.load(f)
        return dictionary_data
    except FileNotFoundError:
        print("Dictionary file not found.")
        return {}

# Function to get the definition of a word
def get_definition(word, dictionary_data):
    # Normalize input by converting the word to lowercase
    word = word.lower()

    # Check if the word exists in the dictionary
    if word in dictionary_data:
        return dictionary_data[word]
    
    # If the word doesn't exist, suggest similar words
    else:
        suggestions = difflib.get_close_matches(word, dictionary_data.keys(), n=1)
        if suggestions:
            return f"Did you mean '{suggestions[0]}'? Definition: {dictionary_data[suggestions[0]]}"
        else:
            return "The word is not in the dictionary and no close matches found."

# Main program function
def main():
    # Load the dictionary data
    dictionary_file = "dictionary.json"  # Replace with the actual path to your JSON file
    dictionary_data = load_dictionary(dictionary_file)

    if dictionary_data:
        # Take user input
        word = input("Enter a word: ")

        # Get and print the definition
        definition = get_definition(word, dictionary_data)
        print(definition)

if __name__ == "__main__":
    main()
