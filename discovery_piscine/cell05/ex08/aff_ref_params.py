#!/usr/bin/env python3

# chmod +x ./discovery_piscine/cell05/ex08/aff_ref_params.py
# ./discovery_piscine/cell05/ex08/aff_ref_params.py



import sys

parameter = sys.argv[1:]

if len(parameter) < 2:
    print("none")
else: 
    for i in reversed(range(len(parameter))):
        print(parameter[i])


