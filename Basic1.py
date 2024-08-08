#integer division and variables
print("Enter two values")
a = int(input())
b = int(input())
print("Choose operation \n 1 addition \n 2 subtraction \n 3 multiplication \n 4 division")
option = int(input())

if option == 1:
    print(a+b)
elif option == 2:
    print(a-b)
elif option == 3:
    print(a*b)
elif option == 4:
    print(a/b)
else:
    print("invalid choice")
