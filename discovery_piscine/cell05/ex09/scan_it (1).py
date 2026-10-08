#!/usr/bin/env python3

# chmod +x ./discovery_piscine/cell05/ex09/scan_it.py
# ./discovery_piscine/cell05/ex09/scan_it.py

import sys


parameters = sys.argv[1:]


if len(parameters) != 2:
    print("none")
else:
    keyword = parameters[0]
    text = parameters[1]


    if keyword not in text:
        print("none")
    else:
        print(text.count(keyword))
