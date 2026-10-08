#!/usr/bin/env python3

# chmod +x ./discovery_piscine/cell05/ex10/parameter_matching.py
# ./discovery_piscine/cell05/ex10/parameter_matching.py



import sys

parameter = sys.argv[1:]


if len(parameter) != 1:
    print("none")
else:
    leparameter = input("What was the parameter? : ").strip()
    if leparameter in parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")