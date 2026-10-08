#!/usr/bin/env python3

# chmod +x ./discovery_piscine/cell05/ex13/append_it.py
# ./discovery_piscine/cell05/ex13/append_it.py

import sys

def main():
   
    args = sys.argv[1:]

    if not args:
        print("none")
        return

    for arg in args:

        if arg.endswith("ism"):
            continue
        
        print(f"{arg}ism")

if __name__ == "__main__":
    main()
