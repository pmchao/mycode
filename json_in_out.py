# This script copies the contents of one JSON file to another


import json

# Open and read the source JSON file
with open('source.json', 'r') as source_file:
    data = json.load(source_file)  # Load the JSON data from the source file

# Write the data to the destination JSON file
with open('destination.json', 'w') as destination_file:
    json.dump(data, destination_file, indent=4)  # Write the data to the destination file with indentation
