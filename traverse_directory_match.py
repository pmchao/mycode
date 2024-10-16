
"""
This Python script navigates through a specified directory and its subdirectories
to find all files that have a particular file extension (e.g., .txt, .log).
It uses the os.walk() method to recursively traverse the directory and checks
if each file has the desired extension. If a file with the given extension is found,
the script adds its full file path to a list, which is then returned.
The script also handles potential errors that might occur during directory traversal
(e.g., permission issues) and prints the total number of files found.
"""
import os  # Importing the os module for interacting with the file system


# Function to find files with a specific extension in a directory and its subdirectories
def find_files_with_extension(directory, extension):
    matched_files = []  # List to store the paths of matched files
    try:
        # Walk through the directory and its subdirectories
        for root, dirs, files in os.walk(directory):
            for file in files:
                # Check if the file ends with the specified extension
                if file.endswith(extension):
                    # If it does, add the full path of the file to the matched_files list
                    matched_files.append(os.path.join(root, file))
    except Exception as e:
        # Print an error message if something goes wrong during the directory traversal
        print(f"An error occurred: {e}")

    return matched_files  # Return the list of matched files


# Example usage of the function
directory = "/Users/peterchao/testdir"  # The directory to search in (change this to your target directory)
extension = ".txt"  # The file extension to look for (e.g., ".txt")
files = find_files_with_extension(directory, extension)  # Call the function with the directory and extension

# Check if any files were found and print them
if files:
    print(f"Found {len(files)} files with extension '{extension}':")  # Print how many files were found
    for file in files:
        print(file)  # Print the full path of each found file
else:
    # If no files are found, print a message saying so
    print(f"No files with extension '{extension}' found in {directory}")
