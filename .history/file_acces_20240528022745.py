import os
import glob

# Define the directory where the files are located
directory = 'C:\Users\Vijay\Pictures\MERN_VIJAY\07. HTML (Level 1) - Part B'

# Get a list of all files in the directory
files = glob.glob(os.path.join(directory, '*'))

# Loop through and process each file
for file_path in files:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content) 