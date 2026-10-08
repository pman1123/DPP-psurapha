#!/usr/bin/env python3

# chmod +x ./discovery_piscine/cell05/ex06/upcase_it.py
# ./discovery_piscine/cell05/ex06/upcase_it.py



import sys

parameter = sys.argv[1:]

# print("Number of parameters :", len(parameter))

if len(parameter) > 0:
    print(parameter[0].upper())
else:
    print("none")