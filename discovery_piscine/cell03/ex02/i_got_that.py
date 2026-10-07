#!/usr/bin/env python3

# chmod +x ./discovery_piscine/cell03/ex02/i_got_that.py
# ./discovery_piscine/cell03/ex02/i_got_that.py


whatyougottasay = input("What you gotta say? : ").strip()

while True:
    if whatyougottasay == "STOP":
        print(";-;")
        break
    else:
        whatyougottasay = input("I got that! Anything else? : ").strip()




#while whatyougottasay != "STOP":
#   whatyougottasay = input("I got that! Anything else? : ").strip()