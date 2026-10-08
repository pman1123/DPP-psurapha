#!/usr/bin/env python3

# chmod +x ./discovery_piscine/cell05/ex09/scan_it.py
# ./discovery_piscine/cell05/ex09/scan_it.py

import sys

# Get all parameters passed to the script
parameters = sys.argv[1:]

# Check if exactly 2 parameters are provided
if len(parameters) != 2:
    print("none")
else:
    keyword = parameters[0]
    text = parameters[1]

    # Check if the keyword exists in the text
    if keyword not in text:
        print("none")
    else:
        # Count and print occurrences
        print(text.count(keyword))
