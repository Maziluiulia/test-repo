a = input("Write something: ")
if a.isalpha():
    print("It is text ")
    print("Its length is")
    print(len(a))
elif (a.isdigit()) and (int(a) % 2 == 0):
     print("It is number and it is even")
else:
    print("It is number and it is odd")
