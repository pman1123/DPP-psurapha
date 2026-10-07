firstnum = input("Please enter the first number: ").strip()
secondnum = input("Please enter the second number: ").strip()
multnum = int(firstnum) * int(secondnum)
print(str(firstnum) + " x " + str(secondnum) + " = " + str(multnum))
if multnum == 0:
    print("The result is equal to zero.")
if multnum < 0:
    print("The result is negative.")
if multnum > 0:
    print("The result is positive.")