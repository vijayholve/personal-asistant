import os
import glob
import random
# Define the directory where the files are located
directory = 'C:/Users/Vijay/Pictures/MERN_VIJAY/09. HTML (Level - 3)'
print(directory)
# Get a list of all files in the directory
files = glob.glob(os.path.join(directory, '*'))

# Loop through and process each file
file=random.choice(files)