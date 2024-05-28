import os
import glob

# Define the directory where the files are located
directory = 'C:\Users\Vijay/Pictures/MERN_VIJAY/09. HTML (Level - 3)'
print(directory)
# Get a list of all files in the directory
files = glob.glob(os.path.join(directory, '*'))

# Loop through and process each file
for file_path in files:
    print(file_path)