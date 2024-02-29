#!/bin/bash

# Get the directory of the script
script_dir="$(dirname "$0")"

# Prompt the user for the folder name
read -p "Enter folder name: " folder_name

# Create the folder in the script's directory
mkdir -p "$script_dir/$folder_name"

# Create a .py file with the same name as the folder
touch "$script_dir/$folder_name/$folder_name.py"

# Create a .cpp file with the same name as the folder
touch "$script_dir/$folder_name/$folder_name.cpp"

# Create a .txt file with the same name as the folder
touch "$script_dir/$folder_name/$folder_name.txt"

echo "Folder '$folder_name' created in '$script_dir' with files: '$folder_name.py', '$folder_name.cpp', '$folder_name.txt'"

