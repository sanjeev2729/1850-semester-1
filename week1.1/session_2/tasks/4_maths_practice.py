# Work out the answers to the three maths problems:

# 1: (4 x 8) x 6
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return(a/b)
# 2: (2^3) / (8/3)

while True:
    print("+, add")
    print("-, subtract")
    print("*, multiply")
    print("/, division")
    print("exit")
    choice = input("enter your choice: ")

    if choice in ["+","-","*","/"]:
        a=float(input("enter 1st number: "))
        b=float(input("enter 2nd number: "))

        if choice =="+":
            print("the result is:",add(a,b))
        elif choice =="-":
            print("the result is:",subtract(a,b))
        elif choice =="*":
            print("the result is:",multiply(a,b))
        elif choice =="/":
            print("the result is:",division(a,b))
    else:
        print("please enter a valid choice")
    if choice=="exit":
        break    

# 3: 27^2 x 19/4


