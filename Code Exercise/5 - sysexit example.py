# example of sys.exit


data = int ( input("Enter a number between 1 and 10: "))

if data >= 1 and data <=10:
    print ("Data entered ok")
else:
    print("Bad data entered - program exiting")
    import sys
    sys.exit()

print ("Good data entered")
