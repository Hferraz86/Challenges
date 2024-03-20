#!/bin/bash

# Path of the directory

echo "Enter the directory path:"
read dir_path

# Requests the number of permissions

echo "Enter the permissions number (e.g.777"
read permissions

#Checks if the directory exists

if [ ! -d "$dir_path" ]; then
  echo "Error: Directory  '$dir_path' not found"
  exit 1
fi

# Go to the specified directory

cd "$dir_path" 

# Change permissions for all files

chmod -R "$permissions" ./* 

#Display the directory contents with the new permissions

ls -l

echo "Permissions changed successfully!"
