try:
    number=int(input("Enter a value: "))
    print("The number entered is: ",number)
except ValueError as ex:
    print("Exception",ex)