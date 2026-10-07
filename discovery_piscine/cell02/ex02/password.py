password = "Python is awesome"
passwordenter = input("Please enter the password: ").strip()
if passwordenter == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")