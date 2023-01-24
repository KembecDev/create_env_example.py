import os
import sys

# File path where the files will be created
path = input("Enter the file path: ")

# Name of existing .env file
env_file = os.path.join(path, ".env")

# Check if the .env file exists
if not os.path.isfile(env_file):
    print("The .env file does not exist in the specified path.")
    sys.exit()

# Name of .env.example file to create
example_file = os.path.join(path, ".env.example")

# Read lines from existing .env file
with open(env_file) as f:
    lines = f.readlines()

# Write lines to .env.example file
with open(example_file, "w") as f:
    for line in lines:
        # If the line contains a value, replace it with "VALUE"
        if "=" in line:
            key, value = line.split("=")
            line = key + "=VALUE"
        f.write(line)
        f.write("\n")