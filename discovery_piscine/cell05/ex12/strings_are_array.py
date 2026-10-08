#!/usr/bin/env python3

# chmod +x ./discovery_piscine/cell05/ex12/strings_are_array.py
# ./discovery_piscine/cell05/ex12/strings_are_array.py


import sys


parameter = sys.argv[1:]

if len(parameter) != 1:
    print("none")
else:
    input_string = parameter[0]
    
    z_count = input_string.count('z')
    
    if z_count == 0:
        print("none")
    else:
        print('z' * z_count)
