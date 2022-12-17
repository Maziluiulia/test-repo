a = input("Write something: ")
if (a.isdigit()) and (int(a) % 2 == 0):
    print("It is number and it is even")
elif (a.isdigit()) and (int(a) % 2 != 0):
    print("It is number and it is odd")
else:
    print("It is text ")
    print("Its length is")
    print(len(a))
