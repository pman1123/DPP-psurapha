#!/usr/bin/env python3

# chmod +x ./discovery_piscine/cell03/ex00/to25.py
# ./discovery_piscine/cell03/ex00/to25.py


number = int(input("Please enter a number less than 25 : ").strip())
if number <= 25:
    while number <= 25:
        print(number)
        number = number + 1
else:
    print("ERROR")