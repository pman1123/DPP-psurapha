#!/usr/bin/env python3

# chmod +x ./discovery_piscine/cell05/ex14/free_range.py
# ./discovery_piscine/cell05/ex14/free_range.py

import sys

parameter = sys.argv[1:]

if len(parameter) != 2:
    print("none")
else:

    start = int(parameter[0])
    end = int(parameter[1])
    

    result = list(range(start, end + 1))
    
    print(result)
