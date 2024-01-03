#!/bin/bash

# Script to create a markdown file with the current date and a provided filename

# Check if a filename was provided as an argument
if [ $# -eq 0 ]; then
    echo "Error: No filename provided."
    echo "Usage: $0 filename"
    exit 1
fi

# Get the current date in YYYY-MM-DD format
CURRENT_DATE=$(date +%Y-%m-%d)

# Concatenate the date and the provided filename
FILENAME="${CURRENT_DATE}_$1.md"

# Check if the file already exists
if [ -f "$FILENAME" ]; then
    echo "Error: $FILENAME already exists."
    exit 1
else
    # Create a new markdown file and add a title
    echo "# Todo - something great is about to be written 🤓" > ./content/posts/$FILENAME
    echo "Markdown file $FILENAME created successfully."
fi