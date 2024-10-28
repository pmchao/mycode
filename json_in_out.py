import json

# Open and read the source JSON file
with open('students_data.json', 'r') as source_file:
    data = json.load(source_file)  # Load the JSON data from the source file

# Write the data to the destination JSON file
with open('destination.json', 'w') as destination_file:
    json.dump(data, destination_file, indent=4)  # Write the data to the destination file with indentation

# Open and read the destination JSON file to print its content
with open('destination.json', 'r') as destination_file:
    destination_data = json.load(destination_file)  # Load the JSON data from the destination file
    print(json.dumps(destination_data, indent=4))  # Pretty-print the JSON content

print("Concluded")
