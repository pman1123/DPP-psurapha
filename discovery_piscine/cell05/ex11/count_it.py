#!/usr/bin/env python3

# chmod +x ./discovery_piscine/cell05/ex11/count_it.py
# ./discovery_piscine/cell05/ex11/count_it.py



import sys

parameter = sys.argv[1:]

if len(parameter) < 1:
    print("none")
else: 

    print("Total parameters : ", len(parameter))

    for i in range(len(parameter)):
        print(parameter[i]+" : ", len(parameter[i]))