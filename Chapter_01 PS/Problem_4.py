import os

# Directory to list ('.' means the current directory)
directory_path = '/'

# os.listdir() returns a list of names (files and folders) in the given path
contents = os.listdir(directory_path)

print(f"Contents of '{directory_path}':")
for item in contents:
    print(item)