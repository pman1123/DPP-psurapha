#!/usr/bin/env python3

# chmod +x ./discovery_piscine/cell03/ex03/advanced_mult.py
# ./discovery_piscine/cell03/ex03/advanced_mult.py


i = 0
while i <= 10:
    print("Table de " + str(i) + ":", end="")
    

    j = 0
    while j <= 10:
        print(" " + str(i * j), end="")
        j += 1

    print()
    i += 1




