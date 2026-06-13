#Calclator
while True:
    print("\n~~~~~~~CALCULATOR~~~~~~~~")
    a=float(input("Enter First Number: "))
    b=float(input("Enter Second Number: "))
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice=input("Choice operation: ")
    if choice=="1":
        print("Result=",a+b)
    elif choice=="2":
        print("Result=",a-b)
    elif choice=="3":
        print("Result=",a*b)
    elif choice=="4":
        if b!=0:
            print("Result=",a/b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid Choice")
    again=input("Do another calculation?(yes/no):")
    if again.lower()!="yes":
        break    