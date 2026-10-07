#!/usr/bin/env python3

# chmod +x ./discovery_piscine/cell03/ex01/multiplication_table.py
# ./discovery_piscine/cell03/ex01/multiplication_table.py


number = int(input("Please enter a number : ").strip())
multiplier = 0

while multiplier <= 12:
    result = number * multiplier
    print(str(number) + " x " + str(multiplier) + " = " + str(result))
    multiplier += 1