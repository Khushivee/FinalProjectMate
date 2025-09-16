first= input("enter 1 num: ")
operator= input("enter operator(+,-,*,%,/): ")
second= input("enter 2 num: ")
first= int(first)
second= int(second)
if operator == "+" :
    print(first + second)
elif operator == "-" :
    print(first - second)
elif operator == "*" :
    print(first * second)
elif operator == "/" :
    print(first / second)
elif operator == "%" :
    print(first % second)
else:
    print("invalid operation")