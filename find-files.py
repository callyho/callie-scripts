import os
import sys

# Usage: python3 </path/to/script.py> <directory to search> <filenamelist.txt>
# This script will search a directory to see if a list of files are present. The list can have full filenames, with extension, or just filenames without an extension.
# If a match with the name + extension is found, this will be reported as an Exact Match
# If a match with just the name is found, this will be reported as a Close Match
# Non matched files will be listed

# Get the directory and filename list from the command line arguments
directory = sys.argv[1]
filename_list_path = sys.argv[2]

# Read the filename list from the text document
with open(filename_list_path, 'r') as f:
    filenames = [line.strip() for line in f.readlines()]

# Initialize lists to store the files found, exact matches, close matches, and not found
found_files = []
exact_matches = []
close_matches = []
not_found_files = []

# Loop through the filenames and search for them in the directory
for filename in filenames:
    # Build the full path to the directory
    file_dir = os.path.abspath(directory)

    # Loop through the files in the directory
    for file in os.listdir(file_dir):
        # Check if the filename matches the current file in the directory
        if file == filename:
            # Add the file to the list of found files and exact matches
            found_files.append(os.path.join(file_dir, file))
            exact_matches.append(os.path.join(file_dir, file))
            break
        # Check if the filename without extension matches the current file in the directory
        elif os.path.splitext(file)[0] == filename:
            # Add the file to the list of found files and close matches
            found_files.append(os.path.join(file_dir, file))
            close_matches.append(os.path.join(file_dir, file))
            break
    else:
        # Add the filename to the list of not found files
        not_found_files.append(filename)

# Print the list of files found and not found
if len(not_found_files) == 0:
    print()
    print(" *** ALL files found! :) ***")
    print()

# Print the summary of matches and non-matches in lists
total_files = len(filenames)
exact_matches_count = len(exact_matches)
close_matches_count = len(close_matches)
not_found_files_count = len(not_found_files)

print("Summary:")
print("Exact matches: {}/{}".format(exact_matches_count, total_files))
print("Close matches: {}/{}".format(close_matches_count, total_files))
print("Files not found: {}/{}".format(not_found_files_count, total_files))
print()

# Print the list of exact matches
if len(exact_matches) > 0:
    print()
    print("   Exact Matches:")
    print()
    for file in exact_matches:
        print("     " + file)

# Print the list of close matches
if len(close_matches) > 0:
    print()
    print("   Close Matches:")
    print()
    for file in close_matches:
        print("     " + file)

# Print the list of not found files
if len(not_found_files) > 0:
    print()
    print("These files were NOT found:")
    print()
    for filename in not_found_files:
        print("     " + filename)
