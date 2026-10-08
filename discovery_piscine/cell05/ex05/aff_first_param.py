#!/usr/bin/env python3



# chmod +x ./discovery_piscine/cell05/ex05/aff_first_param.py
# ./discovery_piscine/cell05/ex05/aff_first_param.py



import sys

parameter = sys.argv[1:]


if len(parameter) > 0:
    print(parameter[0])  
else:
    print("none")       
